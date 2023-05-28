import flask
from flask import Blueprint
import json
from src.lobbyManager import get_public_lobby_list

index_root = Blueprint('index', __name__)

@index_root.route('/', methods=['GET'])
def index():
    if flask.request.method == 'GET':
        # lobby_name, user_name, created_at, participants, id
        testlobbies = [
            {
                'lobby_name': 'lobby1',
                'user_name': 'user1',
                'created_at': '2020-01-01 00:00:00',
                'participants': 1,
                'id': 1
            },
            {
                'lobby_name': 'lobby2',
                'user_name': 'user2',
                'created_at': '2020-01-01 00:00:00',
                'participants': 2,
                'id': 2
            },
            {
                'lobby_name': 'lobby3',
                'user_name': 'user3',
                'created_at': '2020-01-01 00:00:00',
                'participants': 3,
                'id': 3
            }
        ]
        return flask.render_template('index.html', public_lobbies=get_public_lobby_list())