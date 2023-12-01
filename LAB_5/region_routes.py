from flask import Blueprint, request, jsonify, render_template
from db_test import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

region_routes = Blueprint('region', __name__)

# Описание классов в SQLAlchemy моделях


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class CarTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric, nullable=False)


class RegionForm(FlaskForm):
    region_code = IntegerField('Код региона', validators=[DataRequired()])
    name = StringField('Название региона', validators=[DataRequired()])
    submit = SubmitField('Добавить')
    submit_update = SubmitField('Обновить')


class RegionForm_delete(FlaskForm):
    region_code = IntegerField('Код региона', validators=[DataRequired()])
    submit_delete = SubmitField('Удалить')

# Добавление данных в таблицу Регион


@region_routes.route('/v1/region/add', methods=['POST'])
def add_region():
    form = RegionForm(request.form)
    if form.validate_on_submit():
        region_code = form.region_code.data
        name = form.name.data

        if Region.query.filter_by(id=region_code).first():
            message = 'Регион с этим кодом уже существует'
        else:
            region = Region(id=region_code, name=name)
            db.session.add(region)
            db.session.commit()
            message = 'Регион успешно добавлен'
        return render_template('region-add.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('region-add.html', form=form, message=message)


@region_routes.route('/web/region/add', methods=['GET'])
def get_region_add():
    form = RegionForm(request.form)
    return render_template('region-add.html', form=form)

# Обновление данных в таблице Регион


@region_routes.route('/v1/region/update', methods=['POST'])
def update_region():
    form = RegionForm(request.form)
    if form.validate_on_submit():
        region_code = form.region_code.data
        name = form.name.data

        region = Region.query.filter_by(id=region_code).first()
        if not region:
            message = 'Региона с таким кодом не существует'
        else:
            region.name = name
            db.session.commit()

            message = 'Регион успешно обновлен'
        return render_template('region-update.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('region-update.html', form=form, message=message)


@region_routes.route('/web/region/update', methods=['GET'])
def get_region_update():
    form = RegionForm(request.form)
    return render_template('region-update.html', form=form)

# Удаление данных из таблицы Регион


@region_routes.route('/v1/region/delete', methods=['POST'])
def delete_region():
    form = RegionForm_delete(request.form)
    if form.validate_on_submit():
        region_code = form.region_code.data

        # Удаляем запись из таблицы tax_param
        tax_param = CarTaxParam.query.filter_by(city_id=region_code).first()
        if tax_param:
            db.session.delete(tax_param)
            db.session.commit()

        region = Region.query.filter_by(id=region_code).first()
        if not region:
            message = 'Региона с таким кодом не существует'
        else:
            db.session.delete(region)
            db.session.commit()
            message = 'Регион успешно удалён'
        return render_template('region-delete.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('region-delete.html', form=form, message=message)


@region_routes.route('/web/region/delete', methods=['GET'])
def get_region_delete():
    form = RegionForm_delete(request.form)
    return render_template('region-delete.html', form=form)

# Вывести все данные таблицы Регион


@region_routes.route('/web/region', methods=['GET'])
def region_list():
    form = RegionForm(request.form)
    regions = Region.query.all()
    return render_template('region-list.html', regions=regions, form=form)