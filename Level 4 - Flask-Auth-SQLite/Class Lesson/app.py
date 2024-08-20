from flask import Flask, request, jsonify
from models.database import db
from models.user import User
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello World"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(user_name=username).first()
        if user and user.password == password:
            return jsonify({"message":"User authenticated."})

    else:
        return jsonify({"message":"User not found."}), 400

if __name__ == "__main__":
    app.run(debug=True)