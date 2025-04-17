from flask import Flask, jsonify
from flask_migrate import Migrate
from config.settings import Settings
from database.db_connection import Connection
from database.db_sqlalchemy import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Connection.URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Connection.TRACK_MODIFICATIONS

db.init_app(app)
Migrate(app, db)


@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"data": "Hello World"})


if __name__ == "__main__":
    app.run(host=Settings.HOST, port=Settings.PORT, debug=Settings.DEBUG)
