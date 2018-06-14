import random

from flask import Blueprint

from App.ext import db
from App.models import Student, Grade

blueprint = Blueprint('first_name', __name__)

def init_blueprint(app):
    app.register_blueprint(blueprint=blueprint)


@blueprint.route('/')
def hello():
    return 'hello'


