from sqlalchemy.orm import sessionmaker
from dao.DAO import Games
from config import engine


class DataGames:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def name_for_game(self, data):
        try:
            user_id = data.get('user_id')
            name = data.get('name')

            games = Games(user_id=user_id, name=name)

            self.session.add(games)
            self.session.commit()
            self.session.close()
            return {'success'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()
