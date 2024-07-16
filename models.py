"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

default_profile_img = "https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png"

def connect_db(app):
    """ Connect to database """

    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User """

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(25),
                           nullable=False)
    
    last_name = db.Column(db.String(25),
                          nullable=False)
    
    image_url = db.Column(db.String,
                          nullable=False,
                          default=default_profile_img)
    
    posts = db.relationship('Post', backref='user')
    
    def full_name(self):
        """ Returns full name of users """
        return f'{self.first_name} {self.last_name}'
    
class Post(db.Model):
    """ Post """

    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                      nullable=False)
    content = db.Column(db.String,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)