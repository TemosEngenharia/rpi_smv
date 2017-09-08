from flask import Blueprint
from flask import render_template
mod = Blueprint('auth', __name__, url_prefix = '/auth', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('auth.index.html')
