from flask import render_template, flash,redirect,url_for
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
            'author': {'username': 'Mahesh'},
            'body': 'Finished watching Avengers yesterday,its so awesome .'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
