from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class RegisterForm(FlaskForm):
	username = StringField('username',validators=[Required()])
	password = PasswordField('password', validators=[Required()])
	submit = SubmitField("submit")


class LoginForm(FlaskForm):
	username = StringField('username',validators=[Required()])
	password = PasswordField('password', validators=[Required()])
	remember = BooleanField("Remember me")
	submit = SubmitField("submit")
