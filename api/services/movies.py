from flask_restful import Resource
from api.utils.decorators import load_request, dump_request, allow_only_roles
from api.serializers import MoviesSerializer
from api.models import Movies, UserRoles


class CreateMoviesResource(Resource):

    @load_request(MoviesSerializer(many=True, unknown="exclude"))
    def post(self, serialized_payload: list):
        Movies.bulk_insert(serialized_payload)
        return "Inserted", 201

    @allow_only_roles(allowed_roles=[UserRoles.ADMIN])
    @dump_request(MoviesSerializer(many=True))
    def get(self):
        movies = Movies.query.all()
        return movies
