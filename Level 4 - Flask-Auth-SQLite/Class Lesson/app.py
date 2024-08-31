from flask import Flask, request, jsonify
from models.database import db
from models.user import User
from flask_login import LoginManager, login_user, logout_user,current_user, login_required
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

#view login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#log user in
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #Login
        user = User.query.filter_by(user_name=username).first()
        
        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message":"User authenticated."})

    return jsonify({"message":"User not found."}), 400

#log user out
@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "User loged out."})

#creating user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

    if username and password:
        user = User(user_name = username, password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify ({"message": "New user was created" })
    
    return jsonify({"message": "Something got wrong."}), 400

#reading user
@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify({"username": user.user_name})
    
    return jsonify({"message": "User not found"}), 404

#updating user
@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):
    user = User.query.get(id_user)
    data = request.json

    if id_user != current_user.id and current_user.role == 'user':
        return jsonify({"message": "You can NOT change this user's password, because you are NOT an admin."}), 403

    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"message": f"{user.user_name} your password was reseted."})
    return jsonify({"message": "User not found."}), 404

#deleting user
@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if current_user.role == 'user':
        if id_user == current_user.id:
            return jsonify({"message": "You can not delete yourself."}), 403
        return jsonify({"message": "You can NOT delete this user, because you are NOT and admin."}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted."})
    
    return jsonify({"message": "User not found."})


if __name__ == "__main__":
    app.run(debug=True)