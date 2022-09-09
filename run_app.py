from db_request.users import DataUsers
from db_request.games import DataGames
from flasgger import Swagger
from flask import request
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)


def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        create_user = DataUsers().create_user(data=json)
        return create_user
    else:
        return 'Content-Type not supported!'


def create_name_for_game():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        create_user = DataGames().name_for_game(data=json)
        return create_user
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
