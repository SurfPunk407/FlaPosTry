import os
from dotenv import load_dotenv
from flask import Flask 
from .extensions import db
from .routes import main
from .models import User
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    

    db.init_app(app)

    app.register_blueprint(main)

    return app
