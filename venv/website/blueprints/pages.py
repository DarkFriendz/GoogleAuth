#Assets
from flask import Blueprint, render_template, redirect

#Set Blueprint
pages = Blueprint('Pages', __name__, url_prefix='/')

#Index
@pages.route('/')
def index():
    return render_template('home.html')