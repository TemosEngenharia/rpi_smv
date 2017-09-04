from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import jinja2

class MyApp(Flask):
    def __init__(self):
        Flask.__init__(self, __name__)
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter = ".")
        ])
    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp):
        Flask.register_blueprint(self, bp)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader


# Define the WSGI application object
app = MyApp()
app.config.from_object('config')
db = SQLAlchemy(app)
db.create_all()

# Import a module / component using its blueprint handler variable
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprints
app.register_blueprint(auth_module)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 440
