#Assets
from flask import Flask, redirect, url_for, render_template, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from google.oauth2 import id_token
from google.auth.transport import requests

#Class Website
class web():
    #Congig Website
    def __init__(self, config:any):
        #Create Website
        self.web = Flask(__name__)
        
        #Secret Key Website
        self.web.secret_key = config['Website']['Secret']

        #Get Blueprints
        from .blueprints.pages import pages

        #Blueprints
        self.web.register_blueprint(pages)

    #Run Website
    def run(self, debug:bool=False):
        
        #Run
        self.web.run(debug=debug)