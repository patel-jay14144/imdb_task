from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from api.models import UserRoles


class UserSerializer(Schema):
    id = fields.UUID(dump_only=True)
    full_name = fields.String(allow_none=False)
    email_id = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    role = EnumField(UserRoles, required=True)


class SignInSerializer(Schema):
    email_id = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)


class LogInSerializer(Schema):
    access_token = fields.String()
    refresh_token = fields.String()
    user_obj = fields.Nested(UserSerializer)
