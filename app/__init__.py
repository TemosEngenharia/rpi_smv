import importlib
import os
import pkgutil

from flask import Flask
from flask import g
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import jinja2

class MyApp(Flask):
    def __init__(self, implementation):
        Flask.__init__(self, __name__)
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter = ".")
        ])
        def import_dir(path, prefix):
            for _, packege, _ in pkgutil.walk_packages([path]):
                if package[:4] == 'mod_' or package == implementation:
                    for _, module, _ in pkgutil.iter_modules([path + package]):
                        if module == 'controller':
                            controller = importlib.import_module(prefix + '.' + package + '.' + module)
                            if hasattr(controller, 'mod'):
                                self.register_blueprint(controller.mod)
                                print('Registering:', prefix + '.' + package + '.' + module)
        path = os.path.dirname(__file__) + '/'
        import_dir(path, 'app')
        import_dir(path + implementation + '/', 'app.' + implementation)

        @self.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404

        @self.teardown_appcontext
        def close_db(error):
            if hasattr(g, 'cursor'):
                g.cursor.close()
            if hasattr(g, 'database'):
                g.database.close()
            if hasattr(g, 'clientsDB'):
                g.clientsDB.close()

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
