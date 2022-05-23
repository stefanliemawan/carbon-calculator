from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:10posKamehameha!@localhost:5432/carboncal"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Emissions_Per_Item(db.Model):
    index = db.Column(db.String(20), primary_key=True)
    item = db.Column(db.String(20), nullable=False)
    ghg = db.Column(db.Numeric)
    co2 = db.Column(db.Numeric)
    nrg = db.Column(db.Numeric)

    def __repr__(self):
        return f"<Emission_Per_Item {self.item}>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"