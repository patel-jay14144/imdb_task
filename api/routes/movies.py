from api import api
from api.services import AddMoviesResource

api.add_resource(AddMoviesResource, "/movies")