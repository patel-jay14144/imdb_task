from api import api
from api.services import SignInResource, SignUpResource

api.add_resource(SignUpResource, "/users")
api.add_resource(SignInResource, "/users/sign-in")
