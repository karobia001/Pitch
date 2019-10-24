from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User,Comment
from .forms import PitchForm,UpdateProfile,CommentForm
from flask_login import login_required,current_user
from .. import  db,photos

#views
@main.route('/', methods=['GET','POST'])
def index():
    '''
    View root page that returns the index page and its data
    '''
    inspiration=Pitch.query.filter_by(category='inspiration').all()
    interview=Pitch.query.filter_by(category='interview').all()
    pickUp=Pitch.query.filter_by(category='pick-up').all()
    product=Pitch.query.filter_by(category='product').all()
    promotion=Pitch.query.filter_by(category='promotion').all()      
    comments = Comment.query.filter_by(pitch_id=Pitch.id).all()     
    title = 'One Minute Pitch'
    return render_template('index.html',title=title, comments=comments,
                                                     interview = interview,
                                                     inspiration=inspiration,
                                                     pickUp=pickUp,
                                                     product=product,
                                                     promotion=promotion)

@main.route('/create/new', methods = ['GET','POST'])
@login_required
def create():
    '''
    View page that returns a form to create your own pitch
    '''
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        name = form.name.data
        category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitch(title = title,name=name,category=category,
                          pitch=pitch,user=current_user)
        
        #save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    title = 'One Minute Pitch'
    return render_template('create.html',title=title,pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = current_user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/new',methods=['GET','POST'])
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        author = form.author.data
        body = form.body.data
        vote = form.vote.data
        new_comment = Comment(author,body,vote)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    title = f'Comment'
    return render_template('comment.html',title=title,comment = form)