from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OgTcOWAcm0W5IEEJe8g4ec0xqGTullXW'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


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


if __name__ == '__main__':
    app.run(debug=True)
