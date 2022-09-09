from sqlalchemy.orm import sessionmaker
from dao.DAO import Users
from config import engine


class DataUsers:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_user(self, data):
        try:
            username = data.get('username')
            age = data.get('age')
            email = data.get('email')

            user = Users(username=username, age=age, email=email)

            self.session.add(user)
            self.session.commit()
            self.session.close()
            return self
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_user_by_id(self, user_id):
        try:
            user = self.session.query(Users).filter(Users.id == user_id).first()
            return {'id': user.id, 'username': user.username, 'age': user.age, 'email': user.email}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()
