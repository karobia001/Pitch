from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
import time

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())    
    password_hash = db.Column(db.String(255))
    pitch_id = db.relationship('Pitch',backref='user',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    name = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='pitchez',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitch.clear()

    @classmethod
    def get_category(cls,category):
        pitch_cat = Pitch.query.filter_by(category=category).all()
        return pitch_cat

    all_pitch=[]
    def __init__(self,title,name,category,pitch,user):
        self.title=title
        self.name = name
        self.category = category
        self.pitch = pitch
        self.user =user

class Comment(db.Model):

    __tablename__ = 'comments'
    id =db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    body = db.Column(db.String)
    vote = db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))

    all_comments = []
    def __init__(self,author,body,vote):
        self.body = body
        self.vote = vote
        self.author = author

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comment(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.all()
        return comments
        # response = []
        # for comment in cls.all_comments:
        #         response.append(comment)

        # return response