# from .extensions import db
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


log_car = db.Table('log_car',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    db.Column('car_id', db.Integer, db.ForeignKey('car.id'), primary_key=True)
)

# log_food = db.Table('log_food',
#     db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
#     db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
# )

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), unique=True, nullable=False)
    engine = db.Column(db.Float, nullable=False)
    cylinder = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.Float, nullable=False)

    @property
    def speed(self):
        return self.engine * 4 + self.cylinder * 4 + self.fuel * 9


# class Food(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     proteins = db.Column(db.Integer, nullable=False)
#     carbs = db.Column(db.Integer, nullable=False)
#     fats = db.Column(db.Integer, nullable=False)

#     @property
#     def calories(self):
#         return self.proteins * 4 + self.carbs * 4 + self.fats * 9

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cars = db.relationship('Car', secondary=log_car, lazy='dynamic')


# class Log(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date, nullable=False)
#     foods = db.relationship('Food', secondary=log_food, lazy='dynamic')