import os
from flask import Flask
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

# class Emissions_Per_Item(db.Model):
#     index = db.Column(db.String(20), primary_key=True)
#     item = db.Column(db.String(20), nullable=False)
#     ghg = db.Column(db.Numeric)
#     co2 = db.Column(db.Numeric)
#     nrg = db.Column(db.Numeric)

#     def __repr__(self):
#         return f"<Emission_Per_Item {self.item}>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"