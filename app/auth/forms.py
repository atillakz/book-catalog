from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email
from app.auth.models import User

def email_exists(form, field):
    email = User.query.filter_by(user_email = field.data).first()
    if email:
        raise ValidationError("Email already exists")



class RegistrationForm(FlaskForm):

    name = StringField('Whats your name', validators=[DataRequired(),Length(3, 15 , message='between 3 and 15 characters')])

    email = StringField('Enter your e-mail ', validators=[DataRequired(), Email(), email_exists])

    password = PasswordField('Enter password', validators=[DataRequired(), Length(5), EqualTo('confirm',message='password must match')])

    confirm = PasswordField('Confirm', validators=[DataRequired()])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_logged_in = BooleanField('stay logged-in')
    submit = SubmitField('LogIn')
