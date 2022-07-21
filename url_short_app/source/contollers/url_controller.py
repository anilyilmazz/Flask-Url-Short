from flask import request
from flask_restx import Resource

from ..util.dto import UrlDto
from ..services.url_service import get_url, create_url

api = UrlDto.api

@api.route("/")
class UrlView(Resource):
    """
        Url view
    """
    @api.doc('url view')
    def get(self):
        """Present url"""
        return create_url()
