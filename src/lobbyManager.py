from src.app import lobby
import time

def gen_random_letters(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def get_lobby_url_exists(url):
    for l in lobby:
        if l['url'] == url:
            return True
    return False

def add_lobby(lobby_name, user_name, public, password=None):
    while True:
        url = 'lobby/' + gen_random_letters(8)
        if not get_lobby_url_exists(url):
            break
    lobby.append({
        'lobby_name': lobby_name,
        'user_name': user_name,
        'created_at': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        'participants': 0,
        'public': public,
        'password': password,
        'id': len(lobby) + 1,
        'url': url
    })
    return len(lobby)

def get_lobby_by_id(id):
    for l in lobby:
        if l['id'] == id:
            return l
    return None

def get_lobby(id):
    for l in lobby:
        if l['id'] == id:
            return l
    return None

def get_lobby_by_name(lobby_name):
    for l in lobby:
        if l['lobby_name'] == lobby_name:
            return l
    return None

def remove_lobby(id):
    for l in lobby:
        if l['id'] == id:
            lobby.remove(l)
            return True
    return False

def get_lobby_list():
    return lobby

def get_public_lobby_list():
    return [l for l in lobby if l['public']]

def set_participants(id, participants):
    for l in lobby:
        if l['id'] == id:
            l['participants'] = participants
            return True
    return False