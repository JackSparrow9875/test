from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class UserSignup(FlaskForm):
    StringField('Enter Your Name', validators=[data_required()])
    StringField('Enter Your Email ID', validators=[data_required()])
    StringField('Enter a Password', validators=[data_required()])
    StringField('Confirm Password', validators=[data_required()])
    SubmitField('Submit')

class UserLoginForm(FlaskForm):
