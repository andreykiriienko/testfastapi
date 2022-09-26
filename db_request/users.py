from sqlalchemy.orm import sessionmaker

from config import engine
from dao.DAO import Users


class DataUsers:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_user(self, data: dict):
        try:
            name = data.get('name')
            age = data.get('age')
            email = data.get('email')

            user = Users(name=name, age=age, email=email)

            self.session.add(user)
            self.session.commit()

            get_user = self.get_user_by_email(email=email)

            return {'id': get_user['id'], 'name': get_user['name'], 'age': get_user['age'], 'email': get_user['email'],
                    'connected_game': get_user['connected_game']}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_user_by_email(self, email: str):
        try:
            user = self.session.query(Users).filter(Users.email == email).first()

            return {'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email,
                    'connected_game': user.connected_game}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_user_by_id(self, user_id: int):
        try:
            user = self.session.query(Users).filter(Users.id == user_id).first()

            return {'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email,
                    'connected_game': user.connected_game}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_all_users(self):
        try:
            connected = self.session.query(Users).filter(Users.connected_game).all()
            users_dict = {}
            for index, user in enumerate(connected):
                users_dict[user.id] = {'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email,
                                       'connected_game': user.connected_game}
            return users_dict

        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()
