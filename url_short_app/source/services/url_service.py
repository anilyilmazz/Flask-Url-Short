from url_short_app.source.models.url import Url
from .. import db


def create_url():
    new_url = Url(
        url = "url1",
        short_url = "short_url",
        count = 1
    )
    db.session.add(new_url)
    db.session.commit()
    return "Create Url"

def get_url():
    return "Hello World"