from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User,Comment


#views

    return render_template('comment.html',title=title,comment = form)