
from flask import Blueprint
from flask import render_template
mod = Blueprint('ntp', __name__, url_prefix = '/ntp', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('ntp.index.html')
