from flask import jsonify
from app import db
from app.api.v1 import bp
from app.api.v1.auth import basic_auth, token_auth


@bp.route('/v1/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@bp.route('/v1/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204
