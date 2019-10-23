from . import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())    
    password_hash = db.Column(db.String(255))
    pitch_id = db.relationship('Pitch',backref='user',lazy="dynamic")

   
    def __repr__(self):
        return f'User {self.username}'



