from flasgger import SwaggerView, Schema, fields
from run_app import create


class User(Schema):
    id = fields.Int()
    username = fields.Str()
    age = fields.Str()
    email = fields.Str()


class UserPost(Schema):
    username = fields.Str()
    age = fields.Str()
    email = fields.Str()


class UserViewCreate(SwaggerView):
    tags = ['Users']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": UserPost,
        }
    ]
    responses = {
        201: {
            "description": "Successfully created",
            "schema": User
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        user_create = create()
        return user_create

