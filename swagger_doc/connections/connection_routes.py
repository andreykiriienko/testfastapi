from swagger_doc.connections.connection_views import ConnectionViewCreate

from __main__ import app

app.add_url_rule(
    '/connection',
    view_func=ConnectionViewCreate.as_view('connection_create'),
    methods=['POST']
)
