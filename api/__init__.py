import os
import pandas as pd
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import utils as utils

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

class Item_Emission(db.Model):
    __tablename__ = "item_emissions"
    item_index = db.Column(db.String)
    item_id = db.Column(db.String, unique=True, primary_key=True)
    item_name = db.Column(db.String)
    ghg_kgco2e_per_gbp = db.Column(db.Numeric)
    co2_kgco2_per_gbp = db.Column(db.Numeric)
    nrg_kg_oil_equivalent_per_gbp = db.Column(db.Numeric)
    
    def __init__(self, item_index, item_name, ghg_kgco2e_per_gbp, co2_kgco2_per_gbp, nrg_kg_oil_equivalent_per_gbp):
        self.item_id = utils.generate_id(self.__tablename__, db.session.query(Item_Emission).count())
        self.item_index = item_index
        self.item_name = item_name
        self.ghg_kgco2e_per_gbp = ghg_kgco2e_per_gbp
        self.co2_kgco2_per_gbp = co2_kgco2_per_gbp
        self.nrg_kg_oil_equivalent_per_gbp = nrg_kg_oil_equivalent_per_gbp

    def __repr__(self):
        return "<Item_Emission %r>" % self.item_id

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String, unique=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, email, username, password):
        self.user_id = utils.generate_id(self.__tablename__, db.session.query(User).count())
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.user_id

class User_Emission(db.Model):
    __tablename__ = "user_emissions"
    user_emission_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    ghg_kgco2e = db.Column(db.Numeric)
    co2_kgco2 = db.Column(db.Numeric)
    nrg_kg_oil_equivalent = db.Column(db.Numeric)

    def __init__(self, user_id, datetime, ghg_kgco2e, co2_kgco2, nrg_kg_oil_equivalent):
        self.user_emission_id = utils.generate_id(self.__tablename__, db.session.query(User_Emission).count())
        self.user_id = user_id
        self.datetime = datetime
        self.ghg_kgco2e = ghg_kgco2e
        self.co2_kgco2 = co2_kgco2
        self.nrg_kg_oil_equivalent = nrg_kg_oil_equivalent

    def __repr__(self):
        return "<User_Emission %r>" % self.user_emission_id


db.create_all()

item_emissions_df = pd.read_csv("../clean_datasets/item_emissions.csv")

item_emissions_df["item_id"] = [ utils.generate_id("item_emissions", index) for index in item_emissions_df.index]

columns = item_emissions_df.columns.tolist()

columns = columns[-1:] + columns[:-1]

item_emissions_df = item_emissions_df[columns]

item_emissions_df.to_sql("item_emissions", con=db.engine, index=False, if_exists="replace")

db.session.commit()


# import user as user
# import user_emission as user_emission

# app.register_blueprint(user.bp)