from flask import Blueprint, request, jsonify
from region_route import Region
from db_test import db
car_route = Blueprint('car', __name__, url_prefix='/v1/car')


class CarTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric, nullable=False)


@car_route.route('/tax-param/add', methods=['POST'])
def add_car_tax_param():
    data = request.get_json()
    code_rate = data['code_rate']
    region_code = data['region_code']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Регион не найден'}), 400

    car_tax_param = CarTaxParam.query.filter_by(id=code_rate,
                                                city_id=region.id,
                                                from_hp_car=from_hp_car,
                                                to_hp_car=to_hp_car,
                                                from_production_year_car=from_production_year_car,
                                                to_production_year_car=to_production_year_car).first()
    if car_tax_param:
        return jsonify({'error': 'Параметр налога на автомобиль уже существует'}), 400

    new_car_tax_param = CarTaxParam(id=code_rate,
                                    city_id=region.id,
                                    from_hp_car=from_hp_car,
                                    to_hp_car=to_hp_car,
                                    from_production_year_car=from_production_year_car,
                                    to_production_year_car=to_production_year_car,
                                    rate=rate)
    db.session.add(new_car_tax_param)
    db.session.commit()
    return jsonify({'message': 'Параметр налога на автомобиль успешно добавлен'}), 200


@car_route.route('/tax-param/update', methods=['POST'])
def update_car_tax_param():
    data = request.get_json()
    code_rate = data['code_rate']
    region_code = data['region_code']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Регион не найден'}), 400

    car_tax_param = CarTaxParam.query.filter_by(id=code_rate).first()
    if not car_tax_param:
        return jsonify({'error': 'Параметр налога на автомобиль не найден'}), 400

    existing_car_tax_param = CarTaxParam.query.filter_by(city_id=region.id,
                                                         from_hp_car=from_hp_car,
                                                         to_hp_car=to_hp_car,
                                                         from_production_year_car=from_production_year_car,
                                                         to_production_year_car=to_production_year_car).first()
    if existing_car_tax_param and existing_car_tax_param.id != code_rate:
        return jsonify({'error': 'Параметр налога на автомобиль уже существует'}), 400

    car_tax_param.city_id = region.id
    car_tax_param.from_hp_car = from_hp_car
    car_tax_param.to_hp_car = to_hp_car
    car_tax_param.from_production_year_car = from_production_year_car
    car_tax_param.to_production_year_car = to_production_year_car
    car_tax_param.rate = rate

    db.session.add(car_tax_param)
    db.session.commit()
    db.session.rollback()

    return jsonify({'message': 'Параметр налога на автомобиль успешно обновлен'}), 200


@car_route.route('/tax-param/delete', methods=['POST'])
def delete_car_tax_param():
    data = request.get_json()
    code_rate = data['code_rate']

    car_tax_param = CarTaxParam.query.filter_by(id=code_rate).first()
    if not car_tax_param:
        return jsonify({'error': 'Параметр налога на автомобиль не найден'}), 400

    db.session.delete(car_tax_param)
    db.session.commit()
    db.session.rollback()

    return jsonify({'message': 'Параметр налога на автомобиль успешно удален'}), 200


@car_route.route('/tax-param/get', methods=['GET'])
def get_car_tax_param():
    data = request.get_json()
    code_rate = data['code_rate']

    car_tax_param = CarTaxParam.query.filter_by(id=code_rate).first()
    if not car_tax_param:
        return jsonify({'error': 'Параметр налога на автомобиль не найден'}), 400
    return jsonify({'code_rate': car_tax_param.id,
                    'region_code': car_tax_param.city_id,
                    'from_hp_car': car_tax_param.from_hp_car,
                    'to_hp_car': car_tax_param.to_hp_car,
                    'from_production_year_car': car_tax_param.from_production_year_car,
                    'to_production_year_car': car_tax_param.from_production_year_car,
                    'rate': car_tax_param.rate}), 200


@car_route.route('/tax-param/get/all', methods=['GET'])
def get_all_car_tax_params():
    car_tax_params = CarTaxParam.query.all()
    car_tax_params_list = []
    for car_tax_param in car_tax_params:
        car_tax_params_list.append({'code_rate': car_tax_param.id,
                                    'region_code': car_tax_param.city_id,
                                    'from_hp_car': car_tax_param.from_hp_car,
                                    'to_hp_car': car_tax_param.to_hp_car,
                                    'from_production_year_car': car_tax_param.from_production_year_car,
                                    'to_production_year_car': car_tax_param.from_production_year_car,
                                    'rate': car_tax_param.rate}), 200
    return jsonify(car_tax_params_list), 200


@car_route.route('/tax-param/tax/calc', methods=['GET'])
def calculate_tax():
    data = request.get_json()
    horsepower = int(data['horsepower'])
    year = int(data['year'])
    code_rate = data['code_rate']

    tax_object = CarTaxParam.query.filter_by(id=code_rate). \
        filter(CarTaxParam.from_production_year_car <= year). \
        filter(CarTaxParam.to_production_year_car >= year). \
        filter(CarTaxParam.from_hp_car <= horsepower). \
        filter(CarTaxParam.to_hp_car >= horsepower).first()

    if not tax_object:
        return {'error': 'Объект налогообложения по заданным параметрам не найден'}, 400

    tax_rate = tax_object.rate
    tax = horsepower * tax_rate

    return {'tax': tax}, 200

