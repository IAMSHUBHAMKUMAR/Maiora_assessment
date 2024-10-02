
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    type = db.Column(db.String(50))
    joke = db.Column(db.Text)
    setup = db.Column(db.Text)
    delivery = db.Column(db.Text)
    nsfw = db.Column(db.Boolean)
    political = db.Column(db.Boolean)
    sexist = db.Column(db.Boolean)
    safe = db.Column(db.Boolean)
    lang = db.Column(db.String(10))
