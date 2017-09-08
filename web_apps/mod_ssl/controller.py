
from flask import Blueprint
from flask import render_template
mod = Blueprint('ssl', __name__, url_prefix = '/ssl', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('ssl.index.html')
