import logging
import requests


class HipChatHandler(logging.Handler):   # Inherit from logging.Handler

    def __init__(self,params,url):

        logging.Handler.__init__(self)

        self.params = params
        self.url = url


    def emit(self,logrecord):
        p = requests.post(self.url, data={"message": logrecord.getMessage()} ,params=self.params)






