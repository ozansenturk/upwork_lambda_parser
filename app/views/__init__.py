from flask import Blueprint

views_v1 = Blueprint('views', __name__)

from . import upwork
