
from flask import Blueprint
from flask import render_template
mod = Blueprint('ssh', __name__, url_prefix = '/ssh', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('ssh.index.html')
