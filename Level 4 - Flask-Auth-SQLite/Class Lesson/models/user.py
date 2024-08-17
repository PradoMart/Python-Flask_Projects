from app import db

class user(db.Model):
    #campos [type]: ID [integer], Username [string], Password [string]

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String[80], nullable=False, unique=True)
    password = db.Columns(db.String[80], nullable=False)
    