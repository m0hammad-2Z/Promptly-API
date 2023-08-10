import os
from sqlalchemy import Column, ForeignKey, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432') 
DB_USER = os.getenv('DB_USER', 'postgres') 
DB_PASSWORD = os.getenv('DB_PASSWORD', '12345678') 
DB_NAME = os.getenv('DB_NAME', 'promptly') 
DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

db = SQLAlchemy()

def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with app.app_context():
        db.init_app(app)
        db.create_all()

class Prompt(db.Model):

    __tablename__ = 'prompts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    genre_id = Column(Integer, db.ForeignKey("genres.id"), nullable=False)



    def __init__(self, title, content, genre_id):
        self.title = title
        self.content = content
        self.genre_id = genre_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'genre_id': self.genre_id,
            }
    
class Genre(db.Model):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            }