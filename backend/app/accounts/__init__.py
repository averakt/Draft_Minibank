from flask import Blueprint

bp = Blueprint('acc_create', __name__)

from app.accounts import routes
