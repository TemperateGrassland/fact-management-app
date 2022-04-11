from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    facts = db.relationship('Fact', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    left = db.Column(db.String(140))
    rel = db.Column(db.String(140))
    right = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Fact - Left: {}, Relation: {}, Right: {}, Author: {}>'.format(
            self.left,
            self.rel,
            self.right,
            self.user_id)