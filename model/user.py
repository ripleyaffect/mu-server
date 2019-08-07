import datetime

from app import db

from .mixins import ModelUtils


class User(db.Model, ModelUtils):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)

    name = db.Column(db.String(32), nullable=False)
