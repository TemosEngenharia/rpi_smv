from flask import Blueprint
from flask import render_template
mod = Blueprint('api', __name__, url_prefix = '/api', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('api.index.html')
