from flasgger import SwaggerView, Schema, fields
from run_app import create_name_for_game


class Game(Schema):
    id = fields.Int()
    user_id = fields.Int()
    name = fields.Str()


class GamePost(Schema):
    name = fields.Str()


class GameViewCreate(SwaggerView):
    tags = ['Games']
    parameters = [
        {
            "name": "body",
            "in": "body",
            "type": "string",
            "required": True,
            "schema": GamePost,
        }
    ]
    responses = {
        201: {
            "description": "Successfully created",
            "schema": Game
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        game_create = create_name_for_game()
        return game_create
