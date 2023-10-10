from api import db
from sqlalchemy import CheckConstraint, String, Float, BINARY, UniqueConstraint
from sqlalchemy.orm import mapped_column
import uuid


class Movies(db.Model):
    """
    DB Model for storing Movies
    """
    id = mapped_column(String(36), primary_key=True, default=uuid.uuid4)
    director = mapped_column(String(200), nullable=False, index=True)
    name = mapped_column(String(200), nullable=False, index=True)
    imdb_score = mapped_column(Float(1), nullable=False, default=0)
    popularity = mapped_column(Float(1), nullable=False, default=0)

    @staticmethod
    def bulk_insert(movies_list):
        movies_objs = [Movies(**movie) for movie in movies_list]

        db.session.bulk_save_objects(movies_objs)
        db.session.commit()
