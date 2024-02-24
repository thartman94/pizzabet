from flask import Flask, request, jsonfiy, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(80), unique=True, nullable=False)
    email = db.Column(db.string(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email}


db.create_all()


@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonfiy({"message": "test route"}), 200)


@app.route("/user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        user = User(username=data["username"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return make_response(
            {"message": f"Successfully updated user: {id}", "user": user.json()}, 200
        )
    except Exception as e:
        return make_response(
            jsonfiy({"message": "error creating user", "error": e}), 500
        )


@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonfiy({"users": [user.json() for user in users]}), 200)
    except Exception as e:
        return make_response(
            jsonfiy({"message": "error getting users", "error": e}), 500
        )


@app.route("/user/<int:id>", methods=["GET"])
def get_user(id: int):
    try:
        user = User.query.get(id)
        return make_response(jsonfiy({"users": user.json()}), 200)
    except Exception as e:
        return make_response(
            jsonfiy({"message": f"error getting user with id: {id}", "error": e}), 500
        )


@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id: int):
    try:
        user = User.query.get(id)
        if not user:
            return make_response(jsonfiy({"message": "User not found"}), 404)

        data = request.get_json()
        if data.get("username"):
            user.username = data.get("username")
        if user.get("email"):
            data.email = data.get("email")

        db.session.commit()
        return make_response(
            jsonfiy(
                {"message": f"Successfully updated user: {id}", "user": user.json()}
            ),
            200,
        )
    except Exception as e:
        return make_response(
            jsonfiy({"message": f"error updating user with id:{id}", "error": e}), 500
        )


@app.route("/user/<int:id>", methods=["GET"])
def delete_user(id: int):
    try:
        user = User.query.get(id)
        if not user:
            return make_response(jsonfiy({"message": "User not found"}), 404)

        db.session.delete(user)
        db.session.commit()

        return make_response(jsonfiy({"message": "User deleted"}), 200)
    except Exception as e:
        return make_response(
            jsonfiy({"message": f"error deleting user with id: {id}", "error": e}), 500
        )
