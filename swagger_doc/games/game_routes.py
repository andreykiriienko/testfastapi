from swagger_doc.games.game_views import GameViewCreate, GameViewGetAll, ViewGetAllGameAndUsers

from __main__ import app

app.add_url_rule(
    '/game',
    view_func=GameViewCreate.as_view('game_create'),
    methods=['POST']
)

app.add_url_rule(
    '/games',
    view_func=GameViewGetAll.as_view('all_games'),
    methods=['GET']
)

app.add_url_rule(
    '/games/and/users',
    view_func=ViewGetAllGameAndUsers.as_view('all_games_and_users'),
    methods=['GET']
)
