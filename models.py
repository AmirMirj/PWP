from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


log_car = db.Table('log_car',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    db.Column('car_id', db.Integer, db.ForeignKey('car.id'), primary_key=True)
)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), unique=True, nullable=False)
    engine = db.Column(db.Float, nullable=False)
    cylinder = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.Float, nullable=False)

    @property
    def speed(self):
        return self.engine * 4 + self.cylinder * 4 + self.fuel * 9


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cars = db.relationship('Car', secondary=log_car, lazy='dynamic')

