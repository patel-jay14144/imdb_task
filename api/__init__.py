from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()

from api.routes.movies import *

__all__ = [
    "api",
    "db"
]
