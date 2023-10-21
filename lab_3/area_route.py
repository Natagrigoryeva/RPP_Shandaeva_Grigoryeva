from flask import Blueprint, request, jsonify
from region_route import Region
from db_test import db

area_route = Blueprint('area', __name__, url_prefix='/v1/area')


class AreaTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id', ondelete='CASCADE'), nullable=False)
    rate = db.Column(db.Numeric, nullable=False)


@area_route.route('/tax-param/add', methods=['POST'])
def add_tax_param():
    data = request.get_json()
    area_code = data['area_code']
    region_code = data['region_code']
    rate = data['rate']

    region = Region.query.filter_by(id=region_code).first()
    Region
    if not region:
        return jsonify({'error': 'Регион не существует'}), 400

    area_tax_param = AreaTaxParam(id=area_code, city_id=region_code, rate=rate)
    db.session.add(area_tax_param)
    db.session.commit()

    return jsonify({'message': 'Налоговый параметр района успешно добавлен'}), 200


@area_route.route('/tax-param/update', methods=['POST'])
def update_tax_param():
    data = request.get_json()
    region_code = data['region_code']
    rate = data['rate']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Регион не существует'}), 400

    area_tax_param = AreaTaxParam.query.filter_by(city_id=region_code).first()
    if not area_tax_param:
        return jsonify({'error': 'Параметр районного налога не существует'}), 400

    area_tax_param.rate = rate
    db.session.commit()

    return jsonify({'message': 'Налоговый параметр области успешно обновлен'}), 200


@area_route.route('/tax-param/delete', methods=['POST'])
def delete_tax_param():
    data = request.get_json()
    region_code = data['region_code']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Регион не существует'}), 400

    area_tax_param = AreaTaxParam.query.filter_by(city_id=region_code).first()
    if not area_tax_param:
        return jsonify({'error': 'Параметр районного налога не существует'}), 400

    db.session.delete(area_tax_param)
    db.session.commit()

    return jsonify({'message': 'Налоговый параметр области успешно удален'}), 200


@area_route.route('/tax-param/get', methods=['GET'])
def get_area_tax_param():
    data = request.get_json()
    area_code = data['area_code']
    area_tax_param = AreaTaxParam.query.filter_by(id=area_code).first()
    if not area_tax_param:
        return jsonify({'error': 'Параметр районного налога не существует'}), 400
    return jsonify({'code_rate': area_tax_param.id,
                    'region_code': area_tax_param.city_id,
                    'from_hp_car': area_tax_param.rate}), 200


@area_route.route('/tax-param/get/all', methods=['GET'])
def get_all_area_tax_param():
    area_tax_params = AreaTaxParam.query.all()
    area_tax_params_list = []
    for area_tax_param in area_tax_params:
        area_tax_params_list.append({'code_rate': area_tax_param.id,
                                    'region_code': area_tax_param.city_id,
                                    'from_hp_car': area_tax_param.rate}), 200
        return jsonify(area_tax_params_list), 200


@area_route.route('/tax/calc', methods=['GET'])
def calculate_area_tax():
    data = request.get_json()
    region_code = data['region_code']
    cadastre_value = int(data['cadastre_value'])

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Region does not exist'}), 400
    area_tax_param = AreaTaxParam.query.filter_by(city_id=region_code).first()
    tax_amount = cadastre_value * area_tax_param.rate
    return jsonify({'tax_amount': tax_amount}), 200