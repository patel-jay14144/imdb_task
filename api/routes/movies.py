from api import api
from api.services import CreateMoviesResource

api.add_resource(CreateMoviesResource, "/movies")
