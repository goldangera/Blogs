from . import main
from ..models import User,Post,Comment
from .. import db
from .forms import PostForm,CommentForm
from flask import render_template,redirect,url_for,abort
from flask_login import login_required,current_user
from ..email import mail_message
import datetime
import json 
import requests

@main.route('/')
def index():
    '''
    view root page function that returns index page & data
    '''
    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()

    title = 'Home - Welcome to the SUPER BLOG POST '
    
    random=requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return render_template('index.html',index=index, title=title, post=post, random=random)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,date = user_joined)

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

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
   user = User.query.filter_by(username = uname).first()

   if 'photo' in request.files:
       filename = photos.save(request.files['photo'])
       path = f'photos/{filename}'
       user.profile_pic_path = path
       db.session.commit()

   return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        text = post_form.text.data
        

        # Updated post instance
        new_post = Post(title=title,text=text)

        # Save post method
        new_post.save_post()
        return redirect(url_for('.index'))

    title = 'New post'
    return render_template('new_post.html',title = title,post_form=post_form )


