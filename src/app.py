# -*- coding: utf-8 -*-
import flask
import json

from os.path import dirname, abspath
import sys
sys.path.extend([dirname(dirname(dirname(abspath(__file__)))), dirname(dirname(abspath(__file__)))])

print('flask version', flask.__version__)
app = flask.Flask(__name__, template_folder='templates')
app.secret_key = b'secret_key_sample'

# modules
from lobbyManager import *
lobby = []

# modules-routes
from src.routes.indexRoute import index_root
from src.routes.createRoute import create_root

app.register_blueprint(index_root)
app.register_blueprint(create_root)

# print all routes
print('routes:')
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)