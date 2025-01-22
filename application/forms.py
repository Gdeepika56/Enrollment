from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confrim = PasswordField('Confrim Password', validators=[DataRequired()])
    first_name = PasswordField('First Name', validators=[DataRequired()])
    last_name = PasswordField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register Now')    