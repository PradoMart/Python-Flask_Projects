from models.database import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    #campos [type]: id [Int], Nome [string], Descrição [String], Data e Hora [datetime], Dentro ou não da dieta [Boolean]

    #user data
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
