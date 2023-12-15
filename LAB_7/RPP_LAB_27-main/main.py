from signup import signup
from login import login
from db import db, login_manager
from limit import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/LAB_6'

app.register_blueprint(signup)
app.register_blueprint(login)

app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = 'aboba'

login_manager.init_app(app)

app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False

db.init_app(app)


# Обработчик запроса на файл favicon.ico
@app.route('/favicon.ico')
def favicon():
    return ''


if __name__ == '__main__':
    app.run(debug=True)
