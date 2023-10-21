from flask import Blueprint, request, jsonify
from db_test import db
region_route = Blueprint('region', __name__, url_prefix='/v1/region')


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


@region_route.route('/add', methods=['POST'])
def add_region():
    data = request.get_json()
    region_code = data['region_code']
    name = data['name']

    if Region.query.filter_by(id=region_code).first():
        return jsonify({'error': 'Регион с этим кодом уже существует'}), 400
    region = Region(id=region_code, name=name)
    db.session.add(region)
    db.session.commit()
    return jsonify({'error': 'Регион успешно добавлен'}), 200



@region_route.route('/update', methods=['POST'])
def update_region():
    data = request.get_json()
    region_code = data['region_code']
    name = data['name']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Региона с таким кодом не существует'}), 400
    region.name = name
    db.session.commit()
    return jsonify({'message': 'Регион успешно обновлен'}), 200


@region_route.route('/delete', methods=['POST'])
def delete_region():
    data = request.get_json()
    region_code = data['region_code']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Региона с таким кодом не существует'}), 400
    db.session.delete(region)
    db.session.commit()
    return jsonify({'message': 'Регион успешно удален'}), 200


@region_route.route('/get', methods=['GET'])
def get_region():
    data = request.get_json()
    region_code = data['region_code']

    region = Region.query.filter_by(id=region_code).first()
    if not region:
        return jsonify({'error': 'Региона с таким кодом не существует'}), 400
    return jsonify({'region_code': region.id, 'name': region.name}), 200


@region_route.route('/get/all', methods=['GET'])
def get_all_regions():
    regions = Region.query.all()
    regions_list = []
    for region in regions:
        regions_list.append({'region_code': region.id, 'name': region.name})
    return jsonify(regions_list), 200



