from flask import Flask
from services import parser
import os
from dotenv import load_dotenv
from flask import render_template

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__)


@app.route('/')
def hello_world():

    a_dict = parser.extract_feeds(
                                os.getenv("search_key"),
                                os.getenv("security_token"),
                                os.getenv("user_uid"))

    return render_template('index.html', a_dict=a_dict)
    # return list.summary_detail.value



if __name__ == '__main__':
    app.run()
