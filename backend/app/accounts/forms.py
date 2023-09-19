from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from wtforms import PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask_babel import _, lazy_gettext as _l
from app.models import User


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class Acc_Create(FlaskForm):
    username = StringField(_l('Логин'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторите Пароль'), validators=[DataRequired(),
                                           EqualTo('Пароль')])
    submit = SubmitField(_l('Открыть счет'))    
