import flask
from flask import Blueprint
from src.lobbyManager import get_lobby_list, add_lobby, get_lobby_by_id
import json

create_root = Blueprint('create', __name__)

@create_root.route('/create', methods=['POST'])
def index():
    if flask.request.method == 'POST':
        name = flask.request.form['lobby_name']
        user = flask.request.form['user_name']
        if 'password' in flask.request.form:
            pw = flask.request.form['password']
        else:
            pw = None
        if 'public' in flask.request.form:
            public = True
        else:
            public = False
        print(name, user, pw, public)
        if pw == '':
            pw = None
        id = add_lobby(name, user, public, pw)
        return flask.redirect(get_lobby_by_id(id)['url'])