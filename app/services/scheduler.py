import time

from app.services import sms
from app.services import parser
import os


def send_job_sms():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    a_dict, sms_jobs = parser.extract_feeds(

        os.getenv("search_key"),
        os.getenv("security_token"),
        os.getenv("user_uid"))

    sms.send_sms(sms_jobs)




# # Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())