from flask import render_template
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Nate'} # fake user
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in Portland, Maine!'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers movie was so shit!'
		}
	]
	return render_template('index.html',
				user=user,
				posts=posts)


