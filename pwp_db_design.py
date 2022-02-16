from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///car_showroom.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    makers_name = db.Column(db.String(35), nullable=False)
    car_type = db.Column(db.String(25), nullable=False)

    cars = db.relationship("Car", back_populates="brand")

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(35), nullable=False)
    country = db.Column(db.String(35), nullable=True)

    cars = db.relationship("Car", back_populates="branch")

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_link = db.Column(db.String, nullable=True)

    cars = db.relationship("Car", back_populates="image")

class Bodytype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=True)

    cars = db.relationship("Car", back_populates="bodytype")

class Fuel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(15), nullable=True)

    cars = db.relationship("Car", back_populates="fuel")

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String, nullable=False)
    mid_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)

    cars = db.relationship("Owner_Status", back_populates="owner")

class Ownerstatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id", ondelete="RESTRICT"))
    car_id = db.Column(db.Integer, db.ForeignKey("car.id", ondelete="RESTRICT"))
    status = db.Column(db.String(15), nullable=False)
    owner_num = db.Column(db.Integer, nullable=False)
    transfer_date = db.Column(db.DateTime, nullable=True)

    cars = db.relationship("Car", back_populates="ownerstatus")
    owner = db.relationship("Owner", back_populates="ownerstatus")

class Car(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # owner_id = db.Column(db.Integer, db.ForeignKey("owner.id", ondelete="SET NULL"))
    # exhibition_id = db.Column(db.Integer, db.ForeignKey("exhibition.id", ondelete="SET NULL"))
    # build_date = db.Column(db.DateTime, nullable=True)
    # brand = db.Column(db.String(128), nullable=False)
    # engine_size = db.Column(db.Float, nullable=False)
    # cylinder = db.Column(db.Integer, nullable=True)

    id = db.Column(db.Integer, primary_key=True)
    registration_num = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    engine_number =db.Column(db.String(25), nullable=False)
    cylinder_count = db.Column(db.Integer, nullable=False)
    chasis_num = db.Column(db.String(35), nullable=True)
    body_color = db.Column(db.String(15), nullable=True)
    mfg_year = db.Column(db.DateTime, nullable=True)
    seating_capacity = db.Column(db.Integer, nullable=True)
    horse_power_cc = db.Column(db.Integer, nullable=False)
    maker_id = db.Column(db.Integer, db.ForeignKey("brand.id", ondelete="SET NULL"))
    owner_car_id = db.Column(db.Integer, db.ForeignKey("ownerstatus.id", ondelete="SET NULL"))
    car_fuel_type_id = db.Column(db.Integer, db.ForeignKey("fuel.id", ondelete="SET NULL"))
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.id", ondelete="SET NULL"))
    image_id = db.Column(db.Integer, db.ForeignKey("image.id", ondelete="SET NULL")) #ToDo: remove me if not needed
    car_body_id = db.Column(db.Integer, db.ForeignKey("bodytype.id", ondelete="SET NULL"))

db.create_all()