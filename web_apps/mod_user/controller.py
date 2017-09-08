
from flask import Blueprint
from flask import render_template
mod = Blueprint('user', __name__, url_prefix = '/user', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('user.index.html')
