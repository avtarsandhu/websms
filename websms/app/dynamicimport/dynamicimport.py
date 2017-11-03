import sys
import logging

logger = logging.getLogger('websms')

#### used to dynamically call module for sms provider
##   Provider name is from cfg file

#class DynamicallyImportModule:

    # ----------------------------------------------------------------------

def DynamicallyImportModule(**kwargs):

    module_name  = kwargs['provider']
    message_text = kwargs['message']
    recipient_list = kwargs['to_send_to']

    """Constructor"""

    sys.path.append(module_name)
    module = __import__(module_name)

    try:
        my_class = getattr(module,'construct_sms')
    except:
        e = sys.exc_info()[0]
        logger.error(e)
    try:
        args = { 'message_text': message_text, 'recipient_list': recipient_list}
        return_code, return_text = my_class(**args)
    except:
        e = sys.exc_info()[0]
        logger.error(e)

    return return_code, return_text

