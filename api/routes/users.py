from api.services import SignUpResource, SignInResource
from api import api


api.add_resource(SignUpResource, "/users")
api.add_resource(SignInResource, "/users/sign-in")