from flask_restx import Namespace, fields

class UrlDto:
    api = Namespace('url', description='url operations')
    url = api.model('url', {
        'url': fields.String(required=True, description='user email address'),
        'short_url': fields.String(required=True, description='user username'),
        'count': fields.String(required=True, description='user password'),
    })
