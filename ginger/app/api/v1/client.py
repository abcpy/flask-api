from app.libs.redprint import Redprint
from flask import request
from validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.libs.error_code import Success

api = Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():
    # 1/0
    # data = request.json
    form = ClientForm().validate_for_api()
    if form.validate():
        promise = {
           ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
