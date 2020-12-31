from flask import render_template
from app import app
from app.forms import LoginForm

user = {'username': 'Ydkulks'}

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Suresh'},
            'body': 'Do anybody know how to start learning flask?'
        },
        {
            'author': {'username': 'Inchara'},
            'body': 'Finished watching Peaky Blinders yesterday,its so awesome .'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
