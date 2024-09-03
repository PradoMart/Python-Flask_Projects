from models.database import db
from models.user import User

from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'health123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:health123@127.0.0.1:3306/Daily-Diet'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

#view login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#login user
@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user:
            login_user(user)
            print(current_user.is_authenticated)

        return jsonify ({"message": "User is authenticated."})
        
    return jsonify({"message": "User not found."}), 400



if __name__ == "__main__":
    app.run(debug=True)