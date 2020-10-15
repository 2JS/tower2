import os
import json

class User:
    def __init__(self, user_id, passwd_hash=None, authenticated=False, authorized=False, master=False):
        self.user_id = user_id
        self.passwd_hash = passwd_hash
        self.authenticated = authenticated
        self.authorized = authorized
        self.master = master

    def __repr__(self):
        r = {
            'user_id': self.user_id,
            'passwd_hash': self.passwd_hash,
            'authenticated': self.authenticated,
            'authorized': self.authorized,
            'master': self.master,
        }
        return str(r)

    def can_login(self, passwd_hash):
        return self.passwd_hash == passwd_hash

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    

USERS = {
    "root": User("root", passwd_hash='fiber2019', authorized=True, master=True),
}

def loadUsers():
    global USERS
    if not os.path.isfile(os.environ['TOWER_CREDENTIALS']):
        return
    with open(os.environ['TOWER_CREDENTIALS'], 'r') as f:
        USERS = json.load(f)

def saveUsers():
    global USERS
    with open(os.environ['TOWER_CREDENTIALS'], 'w') as f:
        json.dump(USERS, f, indent=2)

def addUser(user):
    USERS[user.get_id()] = user
    saveUsers()

def removeUser(user):
    del USERS[user.get_id()]
    saveUsers()

def authorizeUser(user, authorize):
    USERS[user.get_id()].authorized = authorize
    saveUsers()

loadUsers()