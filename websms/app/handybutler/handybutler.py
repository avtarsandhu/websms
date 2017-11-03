import requests
import logging
import configparser
import sys
import os
import re
from hipchat.hipchat import send_to_hipchat

logger = logging.getLogger('websms')


## return value from Module is HTTP code and and a Dictionary of details

response_payload = {}
response_code = 0


def construct_sms(**kwargs):
    message_text = kwargs['message_text']
    recipient_list = kwargs['recipient_list']


    # set up paramaters and read configuration file for access details

    config = configparser.ConfigParser()
    configf = os.path.dirname( os.path.realpath(__file__))  + '/handybutler.cfg'

    # config.read('handybutler.cfg')

    config.read(configf)

    originator=config.get('SETTINGS', 'originator')
    username = config.get('SETTINGS', 'username')
    password = config.get('SETTINGS', 'password')
    customername = config.get('SETTINGS', 'customername')
    multimessage = config.get('SETTINGS', 'multimessage')


    serviceUrl = "http://messenger.handybutler.ch/websms/" + customername + "/sendxml.do"

   # return (200, 2000000)


    # define dictionary for Payload

    payload = {}


    # if recipient list is more than 10 then chunk into groups of 10 and send for each group
    # otherwise send one message  for a group of recipients less than 10
    #

    if len(recipient_list) > 9:

        split_list = [recipient_list[i:i + 10] for i in range(0, len(recipient_list), 10 - 1)]
        split_list[-1].append(split_list[0][0])

        for i, peeps in enumerate(split_list, 1):
            split_recipients = ",".join(peeps)
            payload = {'originator' : originator , 'recipient' : split_recipients, 'message' : message_text,
                       'username' : username , 'password' : password  , 'multimessage' : multimessage}

            args = {'serviceUrl': serviceUrl, 'payload': payload }
            sms_response_code , sms_response_text  = send_sms(**args)
            if sms_response_code is not 200 :
                return sms_response_code, sms_response_text
        return sms_response_code, sms_response_text

    else:
        payload = {'originator': originator, 'recipient': recipient_list, 'message': message_text,
                   'username': username, 'password': password, 'multimessage': multimessage}
        args = {'serviceUrl': serviceUrl, 'payload': payload}
        sms_response_code, sms_response_text = send_sms(**args)
        return sms_response_code, sms_response_text


    # Okay finally we have our list of numbers and text message to be sent
    #


def send_sms(**kwargs):


    serviceUrl  = kwargs['serviceUrl']
    payload = kwargs['payload']


    logger.debug(serviceUrl)
    logger.debug(payload)


    # add message and recipients into Log file

    logger.info(serviceUrl)
    for key , value in payload.items():
        if key == 'recipient' or key =='message':
            logger.info(key)
            logger.info(value)

    r = requests.get(serviceUrl, params=payload)
    logger.debug(r.text)


    if r.status_code is not 200:
        response_payload['Error'] = {}
        response_payload['Error']['Internal '] = 'Could not complete request'
        response_payload['Error']['Error '] = r.text
        response_code = 201
        return response_code, response_payload



    # check actual response body for positive response i.e. <okay id
    # if not ok then send message to hipchat room

    if '<okay' not in  r.text:
        logger.error(r.text)


        hipmsg = 'SMS-Credits bei GLUE sind ausgegangen! _DU_ sofort neue bestellen!''' \
                 ' (Koordinieren mit Backoffice)'

        args = {'hipmsg': hipmsg, 'chatcolour': 'red'}

        try:
            testit = send_to_hipchat(**args)
        except:
            e = sys.exc_info()[0]
            logger.error(e)
            response_payload['Error'] = {}
            response_payload['Error']['Hipchat '] = 'Error'
            response_payload['Error']['Error '] = e
            response_code = 201
            return response_code, response_payload

        response_payload['Error'] = {}
        response_payload['Error']['Internal '] = 'Could not complete request'
        response_payload['Error']['Error '] = hipmsg
        response_code = 201
        return response_code, response_payload


    #   if message response is OK check remaining credits
    #   if credits fallen below 2583 send message to chat room

    if '<okay'  in  r.text:


        findCreditStart = re.search(r'credit=', r.text)
        tmpstr  = r.text[findCreditStart.end() + 1:]

        matchCreditEnd = re.search(r'">', tmpstr)
        remaining_credits = tmpstr[0:matchCreditEnd.end() - 2]

        logger.debug('remaining credits = ' + remaining_credits)



        if int(remaining_credits) < 2583 :

            hipmsg = 'SMS-Credits bei GLUE gehen aus, noch ' + \
            remaining_credits + ' Credits (20 Credits = 1 SMS) übrig. Soll mal jemand neue bestellen...'

            args = {'hipmsg': hipmsg, 'chatcolour': 'yellow'}

            try:
                testit = send_to_hipchat(**args)
            except:
                e = sys.exc_info()[0]
                logger.error(e)
                response_payload['Error'] = {}
                response_payload['Error']['Hipchat '] = 'Error'
                response_payload['Error']['Error '] = e
                response_code = 201
                return response_code, response_payload

            response_payload['Info'] = {}
            response_payload['Info']['Remaining Credits '] = remaining_credits
            response_code = 201
            return response_code, response_payload

        # all has gone well respond back with details and remainign credits

        response_code = 200
        return response_code, remaining_credits


