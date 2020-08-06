from flask import Blueprint


services_v1 = Blueprint('services', __name__)



from . import parser, scheduler, sms

