from flask_restx import Namespace, fields

class UrlDto:
    api = Namespace('url', description='Url Short Api')
    url = api.model('url', {
        'url': fields.String(required=True, description='Original url'),
        'short_url': fields.String(required=False, description='Short Url Value'),
        'count': fields.String(required=False, description='Url Count'),
    })
