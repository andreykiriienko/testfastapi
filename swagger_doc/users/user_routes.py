from swagger_doc.users.user_views import UserViewCreate, UserViewGetById, UserViewGetAll

from __main__ import app

app.add_url_rule(
    '/user',
    view_func=UserViewCreate.as_view('user_create'),
    methods=['POST']
)


app.add_url_rule(
    '/user/<int:user_id>',
    view_func=UserViewGetById.as_view('user_get'),
    methods=['GET']
)


app.add_url_rule(
    '/all/users/connected',
    view_func=UserViewGetAll.as_view('users_get'),
    methods=['GET']
)

