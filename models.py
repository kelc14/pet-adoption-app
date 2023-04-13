"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to the database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for pet database and methods"""
    __tablename__ = 'pets'

    def __repr__(self):
        e = self
        return f"<Pet id={e.id}, name={e.name}, species={e.species}, available={e.available}>"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, 
                           nullable=False)
    species = db.Column(db.Text, 
                           nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, 
                          default = True,
                          nullable=False)
