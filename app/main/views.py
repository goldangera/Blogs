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