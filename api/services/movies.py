from flask_restful import Resource

from api.models import Movies, UserRoles
from api.serializers import MoviesSerializer
from api.utils.decorators import allow_only_roles, dump_request, load_request


class CreateMoviesResource(Resource):
    @allow_only_roles(allowed_roles=[UserRoles.ADMIN])
    @load_request(MoviesSerializer(many=True, unknown="exclude"))
    def post(self, serialized_payload: list):
        Movies.bulk_insert(serialized_payload)
        return "Inserted", 201

    @dump_request(MoviesSerializer(many=True))
    def get(self):
        movies = Movies.query.all()
        return movies
