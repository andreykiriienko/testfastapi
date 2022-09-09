from swagger_doc.games.game_views import GameViewCreate

from __main__ import app

app.add_url_rule(
    '/game/create',
    view_func=GameViewCreate.as_view('games_create'),
    methods=['POST']
)
