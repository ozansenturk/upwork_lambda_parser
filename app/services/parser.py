import feedparser
import logging
import os
import asyncio

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import time
from functools import wraps

def timing(func):

    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time.process_time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time.process_time() - start
            print("{} execution time: {} ms".format(func.__name__,end_*1000 if end_ > 0 else 0))
            # logger.debug("{} execution time: {} ms".format(func.__name__, end_ * 1000 if end_ > 0 else 0))
    return _time_it

async def get_feeds_async(q, paging, security_token, user_uid):

    upwork_url = os.getenv("upwork_url")
    upwork_url = upwork_url.format(q, paging, security_token, user_uid)

    news_feed = feedparser.parse(upwork_url)

    return news_feed

@timing
def extract_feeds(q, security_token, user_uid):

    key_words=q.split(",")
    jobs = {}
    sms_jobs = []
    upwork_url = os.getenv("upwork_url")

    for q in key_words:
        for paging in range(0,20,10):

            upwork_url = upwork_url.format(q, paging, security_token, user_uid)
            news_feed = feedparser.parse(upwork_url)

            #TODO last 2 days
            #TODO concurrency
            len_news = len(news_feed.entries)
            logger.info("len_news {}".format(len_news))

            if len_news>1:
                sub_jobs = {q+":"+entry.title:entry.summary for entry in news_feed.entries}
                # sub_list = ["{} {} {}".format(q,entry.title,entry.link) for entry in news_feed.entries]
                # logger.debug("sub_jobs: {}".format(sub_jobs))
                # print("sub_jobs: {}".format(sub_jobs))
                jobs.update(sub_jobs)
                # sms_jobs= sms_jobs + sub_list

    # sms_jobs_str = ''.join(sms_jobs)
    # logger.info("sms_jobs_str {}".format(sms_jobs_str))

    return jobs, sms_jobs