from wtforms import Form
from app.libs.error_code import ParameterException
from flask import request


class BaseForm(Form):
    def __init__(self):
        super(BaseForm, self).__init__(data=request.json)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

