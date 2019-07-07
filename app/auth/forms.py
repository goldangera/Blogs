from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError 


