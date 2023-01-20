from datetime import datetime
from susiety import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(35), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    comment = db.Column(db.String(100), nullable=False)


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    comment = db.Column(db.String(1000), nullable=False)
