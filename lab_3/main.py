# 1. Запускаем локальный сервер Flask
# 2. Регистрируем  все Blueprint компоненты проекта

from flask import Flask
from region_route import region_route
from car_route import car_route
from area_route import area_route
from db_test import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/LAB_3_RPP'
app.register_blueprint(region_route)
app.register_blueprint(car_route)
app.register_blueprint(area_route)

app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
db.init_app(app)


@app.route('/')
def test_1():
    return 'OK'


# Обработчик запроса на файл favicon.ico
@app.route('/favicon.ico')
def favicon():
    return ''


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


