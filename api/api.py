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

class Emissions_Per_Item(db.Model):
    __tablename__ = "emissions_per_item"
    index = db.Column(db.String, primary_key=True)
    item_name = db.Column(db.String)
    ghg_kgco2e_per_gbp = db.Column(db.Numeric)
    co2_kgco2_per_gbp = db.Column(db.Numeric)
    nrg_kg_oil_equivalent_per_gbp = db.Column(db.Numeric)

    def __repr__(self):
        return '<Emissions_Per_Item %r>' % self.item


@app.route("/", methods=["POST"])
def calculateEmissions():
    data = request.json
    item_name = data["item_name"]
    price = data["price"]

    emission =  Emissions_Per_Item.query.filter_by(item_name=item_name).first()

    ghg_kgco2e = price * emission.ghg_kgco2e_per_gbp
    co2_kgco2 = price * emission.co2_kgco2_per_gbp
    nrg_kg_oil_equivalent = price * emission.nrg_kg_oil_equivalent_per_gbp

    calculated_emissions = {
        "ghg_kgco2e": ghg_kgco2e,
        "co2_kgco2": co2_kgco2,
        "nrg_kg_oil_equivalent": nrg_kg_oil_equivalent
    }

    return calculated_emissions
