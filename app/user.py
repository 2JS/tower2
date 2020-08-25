
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
    "2JS": User("2JS", passwd_hash='fiber2019', authorized=True),
}