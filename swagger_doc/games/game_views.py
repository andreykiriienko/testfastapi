from flasgger import SwaggerView, Schema, fields
from run_app import create_game, get_all_games, all_games_and_users


class Game(Schema):
    id = fields.Int()
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
            "description": "Game successfully created",
            "schema": Game
        },
        403: {
            "description": "Access is denied"
        }
    }

    @staticmethod
    def post():
        return create_game()


class GameViewGetAll(SwaggerView):
    tags = ['Games']
    responses = {
        200: {
            "description": "A list of games",
            "schema": Game
        },
        404: {
            "description": "Games not found"
        }
    }

    @staticmethod
    def get():
        return get_all_games()


class ViewGetAllGameAndUsers(SwaggerView):
    tags = ['Games']
    responses = {
        200: {
            "description": "A list of games with users",
            "schema": Game
        },
        404: {
            "description": "Games not found"
        }
    }

    @staticmethod
    def get():
        return all_games_and_users()
