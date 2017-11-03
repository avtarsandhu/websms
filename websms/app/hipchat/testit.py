import logging
import hipchat

import os
from time import strftime
import sys

log = os.getenv('HOME') + '/' + 'logs' + '/avtartest123' + strftime("_%d_%m_%Y.log")

logging.basicConfig(filename=log,
                    filemode='w')

logger = logging.getLogger('websms')


print(logger.name)


hipmsg = 'ABC-Credits bei GLUE gehen aus, noch 195760 Credits (20 Credits = 1 SMS) übrig. Soll mal jemand neue bestellen...'
chatcolour = 'yellow'



print(sys.path)

print(os.path.dirname(hipchat.__file__))





args = {'hipmsg': hipmsg, 'chatcolour': 'yellow'}
try:
    testit = hipchat.send_to_hipchat(**args)
except:
    e = sys.exc_info()[0]
    logger.error('Exception raised')
    logger.error(e)
    sys.exit(1)