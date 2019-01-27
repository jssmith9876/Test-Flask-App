from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):          # Creates a registration class
    username = StringField('Username',      # User input for the username with validations
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',            # User input for email with validations
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',    # User input for pasword with validations
                             validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',    # User input for to confirm the password and validation to make sure it is the same as password
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')  # Creats a submit button


class LoginForm(FlaskForm):          # Creates a login class
    email = StringField('Email',            # User input for email with validations
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',    # User input for pasword with validations
                             validators=[DataRequired()])

    remember = BooleanField('Remember Me')  # Creates a remember me option

    submit = SubmitField('Login')  # Creats a submit button
