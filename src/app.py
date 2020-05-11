from flask import Flask
from blueprints.sensors.DHT import DHT_BLUEPRINT
from blueprints.system import STATUS_BLUEPRINT
from livereload import Server

app = Flask(__name__)
app.register_blueprint(DHT_BLUEPRINT)
app.register_blueprint(STATUS_BLUEPRINT)

if __name__ == "__main__":
    app.run()
