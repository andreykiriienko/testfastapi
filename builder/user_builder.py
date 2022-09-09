from db_request.db_fabric import FabrikDB
import dto.DTO as dto
from dataclasses import asdict
import json


class UserBuilder:
    def __init__(self):
        self.db = FabrikDB
        self.dto_user = dto.Users()
        self.dto_game = dto.Games()

    def get_user_by_id(self, user_id):
        user = self.db.get_user_by_id(user_id=user_id)
        if 'error' not in user:
            self.dto_user.id = user_id
            self.dto_user.name = user['name']
            self.dto_user.age = user['age']
            self.dto_user.email = user['email']
            return self
        else:
            return self

    def to_json(self):
        if self.dto_user.id == 0:
            return json.dumps({'error': ['something went wrong while processing the user']})
        else:
            dto_user = json.dumps(asdict(self.dto_user))
            return json.loads(dto_user)
