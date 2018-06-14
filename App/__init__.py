from flask import Flask

from App import setting
from App.ext import init_ext
from App.views import init_blueprint


def create_app():

    app = Flask(__name__)
    app.config.from_object(setting.envs.get('develop'))
    init_blueprint(app)
    init_ext(app)

    return app