from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import flask_whooshalchemyplus


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e1e0fa76bc39986acb810e80cb78420f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['DEBUG'] = True
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aromasyed12@gmail.com'
app.config['MAIL_PASSWORD'] = 'billgates12345'

mail = Mail(app)

from flaskapp import routes
