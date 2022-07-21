from .. import db

class Url(db.Model):
    """
    Url Model for short url
    """
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(500), unique=True, nullable=False)
    short_url = db.Column(db.String(500), unique=True, nullable=False)
    count = db.Column(db.Integer)
