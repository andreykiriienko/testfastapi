from db_request.users import DataUsers
from db_request.games import DataGames


class FabrikDB(DataUsers, DataGames):
    pass
