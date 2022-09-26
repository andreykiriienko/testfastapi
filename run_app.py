from db_request.users import DataUsers
from db_request.games import DataGames
from db_request.connection import DataConnection
from flasgger import Swagger
from misc import error_processing
from flask import request
from flask import Flask

app = Flask(__name__)
Swagger(app)


def create_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        user = DataUsers().create_user(data=json)
        return error_processing(user, 201, 403)
    else:
        return 'Content-Type not supported!'


def get_user(user_id):
    user_data = DataUsers().get_user_by_id(user_id=user_id)
    return error_processing(user_data, 200, 404)


def get_all_users_connected():
    users = DataUsers().get_all_users()
    return error_processing(users, 200, 404)


def create_game():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        game = DataGames().create_game(data=json)
        return error_processing(game, 201, 403)
    else:
        return 'Content-Type not supported!'


def get_all_games():
    all_game = DataGames().get_all_games()
    return error_processing(all_game, 200, 404)


def all_games_and_users():
    games_and_users = DataGames().get_all_games_and_users()
    return error_processing(games_and_users, 200, 404)


def create_connection():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        connection = DataConnection().create_connection(data=json)
        return error_processing(connection, 201, 403)
    else:
        return 'Content-Type not supported!'


import swagger_doc.users.user_routes
import swagger_doc.games.game_routes
import swagger_doc.connections.connection_routes

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', debug=True)

"""
[
    {
        'game_name': [
            {
                'id': 1,
                'name': 'vlad'
            },
            {
                'id': 2,
                'name': 'vlad'
            }
        ],
        'game_name2': [
            {
                'id': 1,
                'name': 'vlad'
            },
            {
                'id': 4,
                'name': 'vlad'
            }
        ]
    }
]
"""

"""
id
user_id
game_id
"""
