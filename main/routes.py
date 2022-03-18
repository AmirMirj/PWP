from flask import Blueprint, render_template, request, redirect, url_for

from cardealership.models import Car, Log, db

from datetime import datetime 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    logs = Log.query.order_by(Log.date.desc()).all()

    log_dates = []

    for log in logs:
        engine = 0.0
        cylinder = 0
        fuel = 0.0
        speed = 0.0

        for car in log.cars:
            engine += car.engine
            cylinder += car.cylinder 
            fuel += car.fuel
            speed += car.speed

        log_dates.append({
            'log_date' : log,
            'engine' : engine,
            'cylinder' : cylinder,
            'fuel' : fuel,
            'speed' : speed
        })

    return render_template('index.html', log_dates=log_dates)

@main.route('/create_log', methods=['POST'])
def create_log():
    date = request.form.get('date')

    log = Log(date=datetime.strptime(date, '%Y-%m-%d'))

    db.session.add(log)
    db.session.commit()

    return redirect(url_for('main.view', log_id=log.id))


@main.route('/add')
def add():
    cars = Car.query.all()

    return render_template('add.html', cars=cars, car=None)


@main.route('/add', methods=['POST'])
def add_post():
    car_brand = request.form.get('car-brand')
    engine = request.form.get('engine')
    cylinder = request.form.get('cylinder')
    fuel = request.form.get('fuel')

    car_id = request.form.get('car-id')

    if car_id:
        car = Car.query.get_or_404(car_id)
        car.brand = car_brand
        car.engine = engine
        car.cylinder = cylinder
        car.fuel = fuel

    else:
        new_car = Car(
            brand=car_brand,
            engine=engine, 
            cylinder=cylinder, 
            fuel=fuel
        )
    
        db.session.add(new_car)

    db.session.commit()

    return redirect(url_for('main.add'))


@main.route('/delete_car/<int:car_id>')
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()

    return redirect(url_for('main.add'))

@main.route('/edit_car/<int:car_id>')
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    cars = Car.query.all()

    return render_template('add.html', car=car, cars=cars)


@main.route('/view/<int:log_id>')
def view(log_id):
    log = Log.query.get_or_404(log_id)

    cars = Car.query.all()

    totals = {
        'engine' : 0.0,
        'cylinder' : 0,
        'fuel' : 0.0,
        'speed' : 0.0
    }

    for car in log.cars:
        totals['engine'] += car.engine
        totals['cylinder'] += car.cylinder
        totals['fuel'] += car.fuel 
        totals['speed'] += car.speed

    return render_template('view.html', cars=cars, log=log, totals=totals)

@main.route('/add_car_to_log/<int:log_id>', methods=['POST'])
def add_car_to_log(log_id):
    log = Log.query.get_or_404(log_id)

    selected_car = request.form.get('car-select')

    car = Car.query.get(int(selected_car))

    log.cars.append(car)
    db.session.commit()

    return redirect(url_for('main.view', log_id=log_id))

@main.route('/remove_car_from_log/<int:log_id>/<int:car_id>')
def remove_car_from_log(log_id, car_id):
    log = Log.query.get(log_id)
    car = Car.query.get(car_id)

    log.cars.remove(car)
    db.session.commit()

    return redirect(url_for('main.view', log_id=log_id))