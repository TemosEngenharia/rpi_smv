
from flask import Blueprint
from flask import render_template
mod = Blueprint('ap', __name__, url_prefix = '/ap', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('ap.index.html')
