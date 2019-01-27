from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# Dummy data to make sure that the posting system works
posts = [
    {
        'author': 'Jordan Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 26, 2019'
    },
    {
        'author': 'Erica Abercrombie',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 27, 2019'
    }
]

# Routes


@app.route("/")         # Home route that will load the home page
@app.route("/home")
def home():
    return render_template(
        'home.html',    # Renders home.html
        posts=posts     # Sends the dummy data we made
    )


@app.route("/about")    # About route that will load the about page
def about():
    return render_template(
        'about.html',   # Renders about.html
        title='About'   # Sends 'About' to title
    )


@app.route("/register", methods=['GET', 'POST'])  # Register route that will load the register page
def register():
    form = RegistrationForm()
    if (form.validate_on_submit()):
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template(
        'register.html',
        title='Register',
        form=form
    )


@app.route("/login", methods=['GET', 'POST'])  # Login route that will load the login page
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        if (form.email.data == 'admin@log.com' and form.password.data == 'password'):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template(
        'login.html',
        title='login',
        form=form
    )
