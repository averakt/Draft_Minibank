from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from app import db
from app.accounts import bp
from app.accounts.forms import Acc_Create
from app.models import User
from app.auth.email import send_password_reset_email

@bp.route('/acc_create', methods=['GET','POST'])
def acc_create():
    form = Acc_Create()
    return render_template('accounts/acc_create.html', title=_('Открыть новый счет'),
                           form=form)
