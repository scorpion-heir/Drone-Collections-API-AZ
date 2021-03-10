from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email 

class UserLoginForm(FlaskForm):
    #email, password, submit
    email = StringField('Email', validators = [DataRequired(),Email()]) #it has to be filled in, and has to be an email 
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

