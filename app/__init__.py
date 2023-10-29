from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'app/static/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.sqlite3'
app.config['SECRET_KEY'] = "kljgT755GH65s"

def getApp():
    return app

db = SQLAlchemy(app)
db.create_all()

print("Welcome to Screening tool")

from app import routes