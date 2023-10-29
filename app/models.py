from app import db

class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50)) 
    media_directory = db.Column(db.String(150))
    account_type = db.Column(db.String(50))

    def __init__(self, username, password, media_directory, account_type):
        self.username = username
        self.password = password
        self.media_directory = media_directory
        self.account_type = account_type