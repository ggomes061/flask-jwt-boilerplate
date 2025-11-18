from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret"),
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", "sqlite://app.db"),
        JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY", "jwt-super-secret")
    )

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app