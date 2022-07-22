from flask import request
from flask_restx import Resource
from flask import redirect

from ..util.dto import UrlDto
from ..services.url_service import get_url, create_url, get_urls, inc_url_count

api = UrlDto.api
_url = UrlDto.url

@api.route("/")
class UrlData(Resource):
    """
        Url Data Management
    """
    @api.doc('Url List')
    @api.marshal_list_with(_url, envelope='data')
    def get(self):
        """Present url"""
        return get_urls()

    @api.expect(_url, validate=True)
    @api.response(201, 'Url successfully created.')
    @api.doc('Create a new url')
    def post(self):
        """Create a new short url"""
        data = request.json
        return create_url(url=data["url"])

@api.route('/<short_url>')
@api.param('url', 'The Short Url')
@api.response(404, 'Url not found.')
class UrlView(Resource):
    """
        Url Redirect
    """
    @api.doc('Redirect to url')
    def get(self, short_url):
        """Redirect to url"""
        url_object = get_url(short_url)
        if not url_object:
            api.abort(404)
        else:
            inc_url_count(url_object)
            return redirect(url_object.url, code=302)
