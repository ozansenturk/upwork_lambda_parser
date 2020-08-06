from . import views_v1
from flask import render_template, request, current_app
from app.services import sms, parser, scheduler
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


upwork_store = {}

@views_v1.route('/')
def hello_world():

    a_dict, sms_jobs = parser.extract_feeds(
                               current_app.config['SEARCH_KEY'],
                                current_app.config['SECURITY_TOKEN'],
                                current_app.config['USER_UID'])

    # sms.send_sms(sms_jobs[0])

    return render_template('index.html', a_dict=a_dict)

@views_v1.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html',
                           error_message='uncaught exception'), 500