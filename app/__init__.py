from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://user:password@localhost/moviesdb"
    )
    db.init_app(app)

    from .routes import movies_bp

    app.register_blueprint(movies_bp)

    return app
