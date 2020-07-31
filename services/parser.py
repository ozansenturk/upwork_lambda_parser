import feedparser
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
def extract_feeds(q, security_token, user_uid):


    jobs = {}
    for paging in range(0,3):
        upwork_url = os.getenv("upwork_url")
        upwork_url = upwork_url.format(q, paging, security_token, user_uid)

        news_feed = feedparser.parse(upwork_url)

        len_news = len(news_feed.entries)

        logger.info("len_news {}".format(len_news))

        if len_news>0:
            sub_jobs = {entry.title:entry.summary for entry in news_feed.entries}
            # logger.debug("sub_jobs: {}".format(sub_jobs))
            print("sub_jobs: {}".format(sub_jobs))
            jobs.update(sub_jobs)



    return jobs