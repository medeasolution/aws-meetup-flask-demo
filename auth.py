class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User: '%s'" % self.username

users = [ 
    User(1, 'admin', 'pass'),
    User(2, 'user', 'helloworld'),
    User(3, 'another', 'user')
]

usersByName = {u.username: u for u in users}
userids = {u.id: u for u in users}

def login(user, password):
    if user in usersByName and usersByName[user].password == password:
        return usersByName[user]

def identity(payload):
    uid = payload['identity']
    return userids.get(uid, None)
