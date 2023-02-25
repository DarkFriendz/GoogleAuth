#Assets
from flask import Flask

#Class Website
class web():
    #Config Website
    def __init__(self, config:any):
        #Created Website
        self.web = Flask(__name__)

    #Run Website
    def run(self, debug:bool=False):

        #Run
        self.web.run(debug=debug)