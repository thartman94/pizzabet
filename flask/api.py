from flask import  request, jsonify, make_response, Blueprint

from models import db
from models.user import User
from models.payment import Payment
from models.bet import Bet


api = Blueprint("api", __name__)

@api.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return make_response(user.json(), 200)


@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return make_response({"users": [user.json() for user in users]}, 200)


@api.route("/user/<int:id>", methods=["GET"])
def get_user(id: int):
    user = User.query.get(id)
    return make_response(jsonify({"users": user.json()}), 200)


@api.route("/user/<int:id>", methods=["PUT"])
def update_user(id: int):
    user = User.query.get(id)
    if not user:
        return make_response(jsonify({"message": "User not found"}), 404)

    data = request.get_json()
    if data.get("username"):
        user.username = data.get("username")
    if data.get("email"):
        user.email = data.get("email")

    db.session.commit()
    return make_response(
        jsonify({"message": f"Successfully updated user: {user.id}", "user": user.json()}),
        200,
    )



@api.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id: int):
    user = User.query.get(id)
    if not user:
        return make_response(jsonify({"message": "User not found"}), 404)

    db.session.delete(user)
    db.session.commit()

    return make_response(jsonify({"message": "User deleted"}), 200)

