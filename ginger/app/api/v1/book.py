from flask import Blueprint
from app.libs.redprint import Redprint

# book = Blueprint('book', __name__)
# @book.route()

"""
  将view 视图注册到redprint
"""
api = Redprint('book')

@api.route('/get')
def get_book():
    return 'get book'