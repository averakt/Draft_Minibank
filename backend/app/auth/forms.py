from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Логин'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Запомнить меня'))
    submit = SubmitField(_l('Войти'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Логин'), validators=[DataRequired()])
    last_name = StringField(_l('Фамилия'), validators=[DataRequired()])
    first_name = StringField(_l('Имя'), validators=[DataRequired()])
    patronymic = StringField(_l('Отчество'))
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторите Пароль'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Зарегистрироваться'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Пожалуйста используйте другое имя пользователя.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Пожалуйста используйте другой email.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Запросить сброс'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторите пароль'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Запросить сброс'))
