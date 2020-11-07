from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Perchè'}
    posts = [
        {
            'author': {'username': 'Lorem'},
            'body': 'Cos’è Lorem Ipsum? Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa.'
        },
        {
            'author': {'username': 'Ipsum'},
            'body': 'Cos’è Lorem Ipsum? Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

