
from flask import Blueprint
from flask import render_template
mod = Blueprint('snmp', __name__, url_prefix = '/snmp', template_folder = 'templates', static_folder = 'static')

@mod.route('/')
def index():
    return render_template('snmp.index.html')
