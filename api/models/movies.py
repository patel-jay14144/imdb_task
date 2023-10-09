from api import db
from sqlalchemy import String, Float, BINARY
from sqlalchemy.orm import mapped_column
import uuid


class Movies(db.Model):
    """
    DB Model for storing Movies
    """
    id = mapped_column(BINARY(16), primary_key=True, default=uuid.uuid4)
    director = mapped_column(String(200), nullable=False, index=True)
    name = mapped_column(String(200), nullable=False, index=True)
    imdb_score = mapped_column(Float(1), nullable=False, default=0)
    popularity = mapped_column(Float(1), nullable=False, default=0)
