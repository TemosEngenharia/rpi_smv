
from flask import Blueprint
from flask import render_template
mod = Blueprint('vpn', __name__, url_prefix = '/vpn', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('vpn.index.html')
