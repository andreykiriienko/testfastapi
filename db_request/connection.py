from sqlalchemy.orm import sessionmaker
from dao.DAO import Connections, Users
from config import engine


class DataConnection:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_connection(self, data: dict):
        try:
            user_id = data.get('user_id')
            game_id = data.get('game_id')

            connection = Connections(user_id=user_id, game_id=game_id)
            user = self.session.query(Users).filter(Users.id == user_id).first()

            if user:
                if user.connected_game is True:
                    self.session.query(Users).filter(Users.id == user_id).update({'connected_game': False})
                else:
                    self.session.query(Users).filter(Users.id == user_id).update({'connected_game': True})

            self.session.add(connection)
            self.session.commit()

            get_connection = self.get_connection_by_id(connection_id=user_id)
            user = self.session.query(Users).filter(Users.id == user_id).first()

            return {'id': get_connection['id'], 'connection': user.connected_game}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_connection_by_id(self, connection_id: int):
        try:
            connection = self.session.query(Connections).filter(Connections.id == connection_id).first()

            return {'id': connection.id}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()
