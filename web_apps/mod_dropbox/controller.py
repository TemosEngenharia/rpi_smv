
from flask import Blueprint
from flask import render_template
mod = Blueprint('dropbox', __name__, url_prefix = '/dropbox', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('dropbox.index.html')
