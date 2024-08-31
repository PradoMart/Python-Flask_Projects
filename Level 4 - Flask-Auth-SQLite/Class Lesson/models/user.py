from models.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    #campos [type]: ID [integer], Username [string], Password [string], Role [string]

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')