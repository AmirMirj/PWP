from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    social_id = db.Column(db.Integer)
    cars = db.relationship('Car', backref='owner')

class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=True)
    business_id = db.Column(db.Integer, nullable=True)
    cars = db.relationship('Car', backref='exhibition')

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    build_date = db.Column(db.DateTime)
    brand = db.Column(db.String(128))
    engine_size = db.Column(db.Float)
    cylinder = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id', ondelete='SET NULL'))
    exhibition_id = db.Column(db.Integer, db.ForeignKey('exhibition.id'))


def populate_db():
    owner1 = Owner(
        name="owner1",
        address="address1",
        social_id=10
    )
    owner2 = Owner(
        name="owner2",
        address="address2",
        social_id=20
    )
    owner3 = Owner(
        name="owner3",
        address="address3",
        social_id=30
    )
    exhb1 = Exhibition(
        name="exhb1",
        address="address1",
        business_id=10
    )
    exhb2 = Exhibition(
        name="exhb1",
        address="address2",
        business_id=20
    )

    car1 = Car(
        build_date=datetime.datetime.now(),
        brand="Toyota",
        engine_size=3.5,
        cylinder=6,
        owner=owner1,
        exhibition=exhb1
    )
    car2 = Car(
        build_date=datetime.datetime.now(),
        brand="Honda",
        engine_size=2.4,
        cylinder=4,
        owner=owner1,
        exhibition=exhb2
    )
    car3 = Car(
        build_date=datetime.datetime.now(),
        brand="hyundai",
        engine_size=2.8,
        cylinder=5,
        owner=owner2,
        exhibition=exhb1
    )

    db.session.add_all([owner1, owner2, owner3, car1, car2, car3, exhb1, exhb2])
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    populate_db()
