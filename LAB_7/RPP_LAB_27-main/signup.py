from flask_wtf import FlaskForm
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from wtforms import StringField, SubmitField, BooleanField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager
from db import db, login_manager

signup = Blueprint('signup', __name__)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))


class UserForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=6, max=32)])
    submit = SubmitField("Зарегестрироваться")


@signup.route('/web/signup', methods=['GET'])
def signup_get():
    form = UserForm(request.form)
    return render_template('signup.html', form=form)

@signup.route('/v1/signup', methods=['POST'])
def signup_1():
    form = UserForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            message =  'Пользователь с указанным email уже существует'
            return render_template('signup.html', form=form, message=message)

        new_user = Users(name=name, email=email, password = generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login.login_get'))

    else:
        message = 'Проверьте правильность введенных данных'
    return render_template('signup.html', form=form, message=message)
