from url_short_app.source.models.url import Url
from .url_short_helper import short_url
from flask import request
from .. import db

def create_url(url):
    response = {"short_url": request.host_url}
    url_object = get_by_origin_url(url)
    if url_object:
        response["short_url"] = response["short_url"] + url_object.short_url
        return response, 200
    shortened_url = short_url(url)
    new_url = Url(
        url=url,
        short_url=shortened_url,
        count=0
    )
    save_changes(new_url)
    response["short_url"] = response["short_url"] + shortened_url
    return response, 200

def inc_url_count(url):
    url.count = url.count + 1
    save_changes(url)

def get_urls():
    return Url.query.all(), 200

def get_url(short_url):
    return Url.query.filter_by(short_url=short_url).first()

def get_by_origin_url(url):
    return Url.query.filter_by(url=url).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
