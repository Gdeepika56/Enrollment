from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6,max=15)])
    password_confrim = PasswordField('Confrim Password', validators=[DataRequired(), Length(min=6,max=15), EqualTo('password')])
    first_name = PasswordField('First Name', validators=[DataRequired()])
    last_name = PasswordField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register Now')    

def validate_Email(self, email):
    user = User.objects(email=email.data).first()
    if user:
        raise ValidationError('Email is already in use. Pick another one.')