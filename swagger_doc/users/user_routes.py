from swagger_doc.users.user_views import UserViewCreate

from __main__ import app

app.add_url_rule(
    '/user/create',
    view_func=UserViewCreate.as_view('users_create'),
    methods=['POST']
)
