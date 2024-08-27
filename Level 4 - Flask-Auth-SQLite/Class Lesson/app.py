from flask import Flask, request, jsonify
from models.database import db
from models.user import User
from flask_login import LoginManager, login_user, logout_user,current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

#view login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #Login
        user = User.query.filter_by(user_name=username).first()
        
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message":"User authenticated."})

    return jsonify({"message":"User not found."}), 400

@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "User loged out."})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(user_name = username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify ({"message": "New user was created" })
    
    return jsonify({"message": "Something got wrong."}), 400

if __name__ == "__main__":
    app.run(debug=True)