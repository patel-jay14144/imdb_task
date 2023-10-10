from flask import Flask
from config import Config
from api import api, db
from api.models import *

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    
    # Load configuration from the Config class
    app.config.from_object(Config)
    api.init_app(app)
    
    db.init_app(app)
    Migrate(app, db)

    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.email_id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(email_id=identity).one_or_none()
        
    return app