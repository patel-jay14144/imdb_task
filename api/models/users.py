import uuid
from enum import Enum

import bcrypt
from flask_restful import abort
from sqlalchemy import Enum as SQLAlchemyENUM
from sqlalchemy import String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import mapped_column

from api import db


class UserRoles(Enum):
    ADMIN = "Admin"
    USER = "User"


class User(db.Model):
    """
    DB Model for storing Users
    """

    id = mapped_column(String(36), primary_key=True, default=uuid.uuid4)
    full_name = mapped_column(String(200), nullable=False, index=True)
    email_id = mapped_column(String(200), nullable=False, unique=True)
    password = mapped_column(String(256), nullable=False)
    role = mapped_column(
        SQLAlchemyENUM(UserRoles), nullable=False, default=UserRoles.USER.name
    )

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.hash_password()  # Automatically hash the password when creating a User instance

    def hash_password(self):
        # Hash the password using bcrypt and set it to the 'password' field
        self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password):
        # Check if the provided password matches the hashed password in the database
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    @staticmethod
    def create(*args, **kwargs):
        try:
            user = User(**kwargs)
            db.session.add(user)
            db.session.commit()
        except IntegrityError as er:
            abort(400, message="User already exists")
