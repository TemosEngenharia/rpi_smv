
from flask import Blueprint
from flask import render_template
mod = Blueprint('net', __name__, url_prefix = '/net', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('net.index.html')
