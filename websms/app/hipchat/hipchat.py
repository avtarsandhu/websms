import logging
from .hipchathandler import HipChatHandler
import configparser
import datetime
import sys
import os


def send_to_hipchat(**kwargs):
    hipmsg = kwargs['hipmsg']
    chatcolour = kwargs['chatcolour']

    logger = logging.getLogger('websms')

    logger.debug('send_to_hipchat')

    config = configparser.ConfigParser()
    configf = os.path.dirname(os.path.realpath(__file__)) + '/hipchat.cfg'



    try:
        # config.read('handybutler.cfg')
        #
        config.read(configf)
    except:
        e = sys.exc_info()[0]
        logger.error(e)
        sys.exit(1)

    try:
        # config.read('handybutler.cfg')
        #
        token = config.get('SETTINGS', 'token')
    except:
        e = sys.exc_info()[0]
        print(e)
        logger.error(e)
        sys.exit(1)


    token = config.get('SETTINGS', 'token')
    url = config.get('SETTINGS', 'url')


    params = {'color': chatcolour, 'auth_token': token}

    logger.debug(token)
    logger.debug(url)
    logger.debug(params)

    chat_handler = HipChatHandler(params, url)  ### create the logging handler object
    chat_handler.setLevel(logging.CRITICAL)     ### set the level at which chatroom messages are sent
    logger.addHandler(chat_handler)             ### add the handler to the logging object

    tt = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")

    logger.critical('CRITICAL  5   ' + hipmsg)
    return