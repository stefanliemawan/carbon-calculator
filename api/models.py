from main import db
import utils as utils

class Item_Emission(db.Model):
    __tablename__ = "item_emissions"
    item_index = db.Column(db.String)
    item_id = db.Column(db.String, unique=True, primary_key=True)
    item_name = db.Column(db.String)
    ghg_kgco2e_per_gbp = db.Column(db.Numeric)
    co2_kgco2_per_gbp = db.Column(db.Numeric)
    nrg_kg_oil_equivalent_per_gbp = db.Column(db.Numeric)

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String, unique=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, email, username, password):
        self.user_id = utils.generate_id("users", db.session.query(User).count())
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class User_Emission(db.Model):
    __tablename__ = "user_emissions"
    user_emission_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    ghg_kgco2e = db.Column(db.Numeric)
    co2_kgco2 = db.Column(db.Numeric)
    nrg_kg_oil_equivalent = db.Column(db.Numeric)

    def __init__(self, user_id, datetime, ghg_kgco2e, co2_kgco2, nrg_kg_oil_equivalent):
        self.user_emission_id = utils.generate_id("user_emissions", db.session.query(User_Emission).count())
        self.user_id = user_id
        self.datetime = datetime
        self.ghg_kgco2e = ghg_kgco2e
        self.co2_kgco2 = co2_kgco2
        self.nrg_kg_oil_equivalent = nrg_kg_oil_equivalent

    def __repr__(self):
        return '<User_Emission %r>' % self.user_emission_id

# how to handle auto increment?