from flask import Flask

# TODO: import config object for Flask project 
from config import Config 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

#import for Flask Login
from flask_login import LoginManager 

#import for AuthLib integrations
from authlib.integrations.flask_client import OAuth 

#import for flsk_marshmallow 
from flask_marshmallow import Marshmallow 

# for REACT
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

# for REACT
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app) #instantiate login manager class after import 
login_manager.login_view = 'signin' #specify what page to load for non-authed users 

oauth = OAuth(app)

ma = Marshmallow(app)

from drone_api import routes, models 