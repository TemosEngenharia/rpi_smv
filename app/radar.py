import sqlite3
import flask

app = flask.Flask(__name__)
app.config.from_object('config')
try:
    app.config.from_envvar('RADAR_CONFIG')
except:
    pass


if __name__ == "__main__":
    app.run()
