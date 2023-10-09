from flask import Flask
from config import Config
from api import api, db
from api.models import *

from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    # Load configuration from the Config class
    app.config.from_object(Config)
    api.init_app(app)
    
    # Initialize any extensions or additional configurations here
    # For example, you might initialize a SQLAlchemy database instance:
    # from flask_sqlalchemy import SQLAlchemy
    # db = SQLAlchemy(app)
    
    # Import and register your blueprints here, if you're using them:
    # from .routes import main_bp, auth_bp
    # app.register_blueprint(main_bp)
    # app.register_blueprint(auth_bp, url_prefix='/auth')



    db.init_app(app)
    Migrate(app, db)
    
    return app