from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.from_pyfile('setting.py')


csrf = CSRFProtect(app)

db = SQLAlchemy(app)

Debugtool = DebugToolbarExtension(app)

from costSummerCamp import view,command

