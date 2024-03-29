from flask import Blueprint, request, render_template
from region_routes import Region, CarTaxParam
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from db_test import db

tax_param = Blueprint('tax_param', __name__)


class TaxParamForm(FlaskForm):
    code_rate = IntegerField('Код параметра', validators=[DataRequired()])
    region_code = IntegerField('Код региона', validators=[DataRequired()])
    from_hp_car = IntegerField('С какого количества лошадиных сил действует объект налогообложения', validators=[DataRequired()])
    to_hp_car = IntegerField('До какого количества лошадиных сил действует объект налогообложения', validators=[DataRequired()])
    from_production_year_car = IntegerField('С какого года производства автомобиля действует объект налогообложения', validators=[DataRequired()])
    to_production_year_car = IntegerField('До какого года производства автомобиля действует объект налогообложения', validators=[DataRequired()])
    rate = FloatField('Налоговая ставка', validators=[DataRequired()])
    submit = SubmitField('Добавить')
    submit_update = SubmitField('Обновить')



class TaxParamForm_delete(FlaskForm):
    code_rate = IntegerField('Код параметра', validators=[DataRequired()])
    submit_delete = SubmitField('Удалить')

# Добавление данных в таблицу Параметр налогообложения


@tax_param.route('/v1/car/tax-param/add', methods=['POST'])
def add_car_tax_param():
    form = TaxParamForm(request.form)
    if form.validate_on_submit():
        code_rate = form.code_rate.data
        region_code = form.region_code.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data

        region = Region.query.filter_by(id=region_code).first()
        if not region:
            message = 'Регион не найден'
        else:
            car_tax_param = CarTaxParam.query.filter_by(id=code_rate,
                                                        city_id=region.id,
                                                        from_hp_car=from_hp_car,
                                                        to_hp_car=to_hp_car,
                                                        from_production_year_car=from_production_year_car,
                                                        to_production_year_car=to_production_year_car).first()
            if car_tax_param:
                message = 'Параметр налога на автомобиль уже существует'
            else:
                new_car_tax_param = CarTaxParam(id=code_rate,
                                                city_id=region.id,
                                                from_hp_car=from_hp_car,
                                                to_hp_car=to_hp_car,
                                                from_production_year_car=from_production_year_car,
                                                to_production_year_car=to_production_year_car,
                                                rate=rate)
                db.session.add(new_car_tax_param)
                db.session.commit()
                message = 'Параметр налога на автомобиль успешно добавлен'
            return render_template('tax-param-add.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('tax-param-add.html', form=form, message=message)


@tax_param.route('/web/tax-param/add', methods=['GET'])
def get_tax_param_add():
    form = TaxParamForm(request.form)
    return render_template('tax-param-add.html', form=form)

# Обновление данных в таблицу Параметр налогообложения


@tax_param.route('/v1/car/tax-param/update', methods=['POST'])
def update_car_tax_param():
    form = TaxParamForm(request.form)
    if form.validate_on_submit():
        code_rate = form.code_rate.data
        region_code = form.region_code.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data

        region = Region.query.filter_by(id=region_code).first()
        if not region:
            message = 'Регион не найден'
        else:
            car_tax_param = CarTaxParam.query.filter_by(id=code_rate).first()
            if not car_tax_param:
                message = 'Параметр налога на автомобиль не найден'
            else:
                existing_car_tax_param = CarTaxParam.query.filter_by(city_id=region.id,
                                                                     from_hp_car=from_hp_car,
                                                                     to_hp_car=to_hp_car,
                                                                     from_production_year_car=from_production_year_car,
                                                                     to_production_year_car=to_production_year_car).first()
                if existing_car_tax_param and existing_car_tax_param.id != code_rate:
                    message = 'Параметр налога на автомобиль уже существует'
                else:
                    car_tax_param.city_id = region.id
                    car_tax_param.from_hp_car = from_hp_car
                    car_tax_param.to_hp_car = to_hp_car
                    car_tax_param.from_production_year_car = from_production_year_car
                    car_tax_param.to_production_year_car = to_production_year_car
                    car_tax_param.rate = rate

                    db.session.add(car_tax_param)
                    db.session.commit()
                    db.session.rollback()

                    message = 'Параметр налога на автомобиль успешно обновлен'
        return render_template('tax-param-update.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('tax-param-update.html', form=form, message=message)


@tax_param.route('/web/tax-param/update', methods=['GET'])
def get_tax_param_update():
    form = TaxParamForm(request.form)
    return render_template('tax-param-update.html', form=form)

# Удаление данных в таблице Параметр налогообложения


@tax_param.route('/v1/car/tax-param/delete', methods=['POST'])
def delete_car_tax_param():
    form = TaxParamForm_delete(request.form)
    if form.validate_on_submit():
        code_rate = form.code_rate.data

        car_tax_param = CarTaxParam.query.filter_by(id=code_rate).first()
        if not car_tax_param:
            message = 'Параметр налога на автомобиль не найден'
        else:
            db.session.delete(car_tax_param)
            db.session.commit()
            db.session.rollback()
            message = 'Параметр налога на автомобиль успешно удален'

        return render_template('tax-param-delete.html', form=form, message=message)

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('tax-param-delete.html', form=form, message=message)


@tax_param.route('/web/tax-param/delete', methods=['GET'])
def get_tax_param_delete():
    form = TaxParamForm_delete(request.form)
    return render_template('tax-param-delete.html', form=form)


# Вывод данных из таблицы Параметр налогообложения


@tax_param.route('/web/tax-param', methods=['GET'])
def get_tax_param_get():
    car_tax_params = CarTaxParam.query.all()
    form = TaxParamForm(request.form)
    return render_template('tax-param-list.html',  car_tax_params=car_tax_params, form=form)