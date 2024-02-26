from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

from models import db
from api import api
from os import environ


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
      db.drop_all()
      db.create_all()
    app.run(debug=True, host='0.0.0.0', port=4000)
