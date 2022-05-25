from api import db

class Emissions_Per_Item(db.Model):
    __tablename__ = "emissions_per_item"
    item_index = db.Column(db.String)
    item_id = db.Column(db.String, primary_key=True)
    item_name = db.Column(db.String)
    ghg_kgco2e_per_gbp = db.Column(db.Numeric)
    co2_kgco2_per_gbp = db.Column(db.Numeric)
    nrg_kg_oil_equivalent_per_gbp = db.Column(db.Numeric)

    def __repr__(self):
        return '<Emissions_Per_Item %r>' % self.item

class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

class User_Emissions(db.Model):
    __tablename__ = "user_emissions"
    user_emission_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    ghg_kgco2e = db.Column(db.Numeric)
    co2_kgco2 = db.Column(db.Numeric)
    nrg_kg_oil_equivalent = db.Column(db.Numeric)

# How to best calculate user emissions?