import phonenumbers
import re
import logging

logger = logging.getLogger('websms')



def clean_and_format_recipients(**kwargs):

    recipient  = kwargs['recipient']


    # final list of recipients once parsed recipients is cleaned and validated


    to_send_to = []

    # create a list of raw numbers by splitting recipient string separetd by commas

    raw_numbers = recipient.split(",")

    logger.debug('number of MSISDNS in raw string = ' + str(len(raw_numbers)))


    # iterate through numbers remove erroneus numbers

    for i, item in enumerate(raw_numbers):

        PhoneRegex = re.compile(r'^(?:\+\d{1,3}|0\d{1,3}|00\d{1,2})?(?:\s?\(\d+\))?(?:[-\/\s.]|\d)+$')
        result = PhoneRegex.search(item)

        # if number is OK format to e164 standard and add to converted list

        if result is not None:
            converted = convert_to_e164(item)
            to_send_to.append(converted)

    # finally remove duplicate numbers from list

    to_send_to = list(set(to_send_to))

    logger.debug('number of MSISDNS in cleaned and formatted list  = ' + str(len(to_send_to)))

    return(to_send_to ,str(len(raw_numbers)), str(len(to_send_to)))


def convert_to_e164(raw_phone):


    '''convert number to  E.164 standard :

            A telephone number can have a maximum of 15 digits
            The first part of the telephone number is the country code (one to three digits)
            The second part is the national destination code (NDC)split_list
            The last part is the subscriber number (SN)
            The NDC and SN together are collectively called the national (significant) number
            Country code: +41
            National destination code: 7621
            Subscriber number: 55989

            i.e  +41762155989       '''



    if not raw_phone:
        return

    if raw_phone[0] == '+':

        # Phone number may already be in E.164 format.
        parse_type = None
    else:
        # If no country code information present, assume it's a swiss number
        parse_type = "CH"

    try:
        phone_representation = phonenumbers.parse(raw_phone, parse_type)
        return phonenumbers.format_number(phone_representation,
            phonenumbers.PhoneNumberFormat.E164)
    except:
        return raw_phone