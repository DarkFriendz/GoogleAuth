#Assets
from flask import Flask, render_template, redirect

#Class Website
class web():
    #Config Website
    def __init__(self, config:any):
        #Created Website
        self.web = Flask(__name__)

    #Run Website
    def run(self, debug:bool=False):

        @self.web.route('/')
        def index():
            return render_template('home.html')

        #Run
        self.web.run(debug=debug)