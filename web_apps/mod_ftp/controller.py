
from flask import Blueprint
from flask import render_template
mod = Blueprint('ftp', __name__, url_prefix = '/ftp', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('ftp.index.html')
