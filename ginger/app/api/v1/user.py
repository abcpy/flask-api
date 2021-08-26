from flask import Blueprint
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User
from app.libs.error_code import NotFount
from flask import jsonify
from app.models.base import db
from app.libs.error_code import DeleteSuccess
from flask import g

"""
用户
客户端 client
"""
# user = Blueprint('user', __name__)

api =Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # token 是否过期 是否合法
    # token
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    # token 是否过期 是否合法
    # token
    user = User.query.get_or_404(uid)
    return jsonify(user)

@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()



