import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
oid = OpenID(app, '~/inez/microblog/flask/flask_openid.py', safe_roots=[])
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
