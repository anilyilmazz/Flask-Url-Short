from flask_restx import Api
from flask import Blueprint

from .source.contollers.url_controller import api as url_ns

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title='Url short app',
    version='1.0',
    description='url short app with flask'
)

api.add_namespace(url_ns, path="/")
