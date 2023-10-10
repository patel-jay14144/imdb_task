from flask_restful import Resource, abort
from api.utils.decorators import load_request, allow_only_roles, dump_request
from api.serializers import UserSerializer, SignInSerializer, LogInSerializer
from api.models import User
from flask_jwt_extended import create_refresh_token, create_access_token


class SignUpResource(Resource):

    @load_request(UserSerializer())
    def post(self, serialized_payload: dict):
        User.create(**serialized_payload)
        return "Signed Up", 201


class SignInResource(Resource):

    @load_request(SignInSerializer())
    @dump_request(LogInSerializer())
    def post(self, serialized_payload: dict):

        user = User.query.filter(User.email_id==serialized_payload["email_id"]).first() or abort(404)
        if not user.check_password(serialized_payload["password"]):
            abort(400, message="Incorrect Password")

        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        return {"access_token": access_token, "refresh_token": refresh_token, "user_obj": user}
