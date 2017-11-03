from flask import Flask
from flask import request
from flask import jsonify
import logging
import os
from time import strftime
from phonefilter.phonefilter import clean_and_format_recipients
from dynamicimport.dynamicimport import  DynamicallyImportModule
from flask_cors import CORS, cross_origin

app = Flask(__name__,instance_relative_config=True)
CORS(app)
app.config.from_pyfile("smsapp.cfg")

## setup logging information from config file

log = os.getenv('HOME') + '/' + 'logs' + '/' + app.config["LOGFILENAME"] + strftime("_%d_%m_%Y.log")
logging.basicConfig(filename=log,filemode='w')
logger = logging.getLogger('websms')
logger.setLevel(app.config["LOGLEVEL"])

# get the sms service povider from config file

provider = app.config["PROVIDER"]

@app.route('/sms' , methods=['GET', 'POST'])
def api_sms():

# validate recipient and message
    response_payload = {}

    recipient = request.args.get('recipient', None)
    message   = request.args.get('message',None)

    if recipient is None and message is None:
        response_payload['error'] = {}
        response_payload['error']['No Message text or Recipents recieved'] = ''
        resp = jsonify(response_payload)
        resp.status_code = 400
        return resp
    elif recipient is None:
        response_payload['error'] = {}
        response_payload['error']['No Recipents recieved'] = ''
        resp = jsonify(response_payload)
        resp.status_code = 400
        return resp
    elif message is None :
        response_payload['error'] = {}
        response_payload['error']['No Message Text recieved'] = ''
        resp = jsonify(response_payload)
        resp.status_code = 400
        return resp

    args = {'recipient':recipient}
    numbers = clean_and_format_recipients(**args)

    to_send_to = numbers[0]
    numbers_in = numbers[1]
    numbers_out =numbers[2]

## check cleaned recipients list to ensure that we still have at least one person to send to

    if len(to_send_to) == 0 :
        response_payload['error'] = {}
        response_payload['error']['Erroneus Recipient List received , No Valid Recipents'] = ''
        response_payload['error']['Invalid Recipients List '] = recipient
        resp = jsonify(response_payload)
        resp.status_code = 400
        return resp


    logger.info('cleaned and formatted recipents = ' + str(to_send_to) +
                ' .Recipents received = ' + str(numbers_in) +
                ' . After filter/clean recipients  = ' + str(numbers_out))
    logger.info('message = ' + message)

    args = {'provider': provider, 'message': message , 'to_send_to' : to_send_to}


    return_code, return_text = DynamicallyImportModule( **args)


    if int(return_code) == 201 :
        response_payload['Info'] = {}
        response_payload['Info']['Recipents received ='] = numbers_in
        response_payload['Info']['message = '] = message
        response_payload['Info']['Remaining Credits are low = '] = return_text
        resp = jsonify(response_payload)
        resp.status_code =  int(return_code)
        return resp
    elif int(return_code)  == 200:
        response_payload['Info'] = {}
        response_payload['Info']['recipients : '] = str(to_send_to)
        response_payload['Info']['message = '] = message
        response_payload['Info']['Remaining Credits = '] = return_text
        resp = jsonify(response_payload)
        resp.status_code = int(return_code)
        return resp
    else:
        response_payload['Error']['Invalid request '] = return_text
        resp = jsonify(response_payload)
        resp.status_code = int(return_code)
        return resp




if __name__ == "__main__":
    app.debug = True
    app.run()




