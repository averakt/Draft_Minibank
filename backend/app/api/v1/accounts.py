from flask import jsonify, request, url_for, abort
from app import db
from app.models import Resource
from app.api.v1 import bp
from app.api.v1.auth import token_auth
from app.api.v1.errors import bad_request

@bp.route('/v1/accounts/<int:id>', methods=['GET'])
@token_auth.login_required
def get_account(id):
    return jsonify(Resource.query.get_or_404(id).to_dict())

@bp.route('/v1/accounts', methods=['POST'])
@token_auth.login_required # TODO убедиться в необходимости
def create_account():
    data = request.get_json() or {}
    if 'brief' not in data or 'name' not in data or 'fund_id' not in data or 'user_id' not in data:
        return bad_request('must include brief, name, fund_id and user_id fields')
    if Resource.query.filter_by(brief=data['brief']).first():
        return bad_request('please use a different brief Resource')
    account = Resource()
    account.from_dict(data, new_account=True)
    db.session.add(account)
    db.session.commit()
    response = jsonify(account.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_account', id=account.id)
    return response


@bp.route('/v1/accounts/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_account(id):
    # Условие ниже не выполнится, т.к. id счета точно не совпадёт с id юзера, убираю этот код
    # if token_auth.current_user().id != id:
    #     abort(403)
    account = Resource.query.get_or_404(id)
    data = request.get_json() or {}
    if 'brief' in data and data['brief'] != account.brief and \
            Resource.query.filter_by(brief=data['brief']).first():
        return bad_request('please use a different brief')
    account.from_dict(data, new_account=False)
    db.session.commit()
    return jsonify(account.to_dict())

@bp.route('/v1/accounts/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_account(id):
    # if token_auth.current_user().id != Resource.query.filter_by(id=id).first():
    #     abort(403)
    # account = Resource.query.get_or_404(id)
    # Resource.query.filter(Resource.id == id).delete()
    Resource.query.filter_by(id=id).delete()
    db.session.commit()
    return '', 204
