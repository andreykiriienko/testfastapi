from sqlalchemy.orm import sessionmaker
from dao.DAO import Games, Users
from config import engine


class DataGames:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_game(self, data: dict):
        try:
            name = data.get('name')
            game = Games(name=name)

            self.session.add(game)
            self.session.commit()

            get_game = self.get_game_by_name(name=name)

            return {'id': get_game['id'], 'name': get_game['name']}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_game_by_name(self, name: str):
        try:
            game = self.session.query(Games).filter(Games.name == name).first()

            return {'id': game.id, 'name': game.name}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_all_games(self):
        try:
            games = self.session.query(Games).all()
            games_dict = {}
            for index, game in enumerate(games):
                games_dict[game.id] = {'id': game.id, 'name': game.name}
            return games_dict
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_all_games_and_users(self):
        try:
            games = self.session.query(Games).all()
            users = self.session.query(Users).filter(Users.connected_game).all()
            games_dict = {}
            for index, game in enumerate(games):
                games_dict[game.id] = {'id': game.id, 'name': game.name}
            return games_dict
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()
