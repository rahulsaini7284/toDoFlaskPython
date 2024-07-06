from model import init_db
from flask_migrate import Migrate
from flask import Flask
from routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    db = init_db(app)

    register_routes(app, db)

    migrate = Migrate(app, db)
    return app
