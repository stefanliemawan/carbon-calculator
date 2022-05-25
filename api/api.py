import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv("../.env")

PSQL_USERNAME = os.environ.get("PSQL_USERNAME")
PSQL_PASSWORD = os.environ.get("PSQL_PASSWORD")
PSQL_HOST = os.environ.get("PSQL_HOST")
PSQL_PORT = os.environ.get("PSQL_PORT")
PSQL_API = os.environ.get("PSQL_API")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{PSQL_USERNAME}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_API}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

engine = db.create_engine(sa_url=app.config["SQLALCHEMY_DATABASE_URI"], engine_opts=app.config["SQLALCHEMY_ENGINE_OPTIONS"])

