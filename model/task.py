import datetime

from app import db

from .mixins import ModelUtils
from .user import User


class Task(db.Model, ModelUtils):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)

    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship(
        User,
        backref=db.backref('tasks', lazy='dynamic'),
        foreign_keys=[user_id])
