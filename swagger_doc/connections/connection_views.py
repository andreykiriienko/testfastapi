from flasgger import SwaggerView, Schema, fields
from run_app import create_connection


class Connection(Schema):
    id = fields.Int()
    connection = fields.Boolean()


class ConnectionPost(Schema):
    user_id = fields.Int()
    game_id = fields.Int()


class ConnectionViewCreate(SwaggerView):
    tags = ['Connection']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": ConnectionPost,
        }
    ]
    responses = {
        201: {
            "description": "Successfully created",
            "schema": Connection
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        return create_connection()
