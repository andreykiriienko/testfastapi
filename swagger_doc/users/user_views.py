from flasgger import SwaggerView, Schema, fields
from run_app import create_user, get_user, get_all_users_connected


class User(Schema):
    id = fields.Int()
    name = fields.Str()
    age = fields.Str()
    email = fields.Str()
    connected_game = fields.Boolean()


class UserPost(Schema):
    name = fields.Str()
    age = fields.Int()
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
            "description": "User successfully created",
            "schema": User
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        return create_user()


class UserViewGetById(SwaggerView):
    tags = ['Users']
    parameters = [
        {
            "name": "user_id",
            "in": "path",
            "type": "string",
            "required": True,
            "default": ""
        }
    ]
    responses = {
        200: {
            "description": "Object of User",
            "schema": User
        },
        404: {
            "description": "Types not found"
        }
    }

    @staticmethod
    def get(user_id):
        return get_user(user_id=user_id)


class UserViewGetAll(SwaggerView):
    tags = ['Users']
    responses = {
        200: {
            "description": "A list of users",
            "schema": User
        },
        404: {
            "description": "Users not found"
        }
    }

    @staticmethod
    def get():
        return get_all_users_connected()
