from . import db,login_manager




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

         return response