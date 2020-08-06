from flask import Flask
from app.services import services_v1
from app.views import views_v1
from config import config
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):

    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)
    application.wsgi_app = ProxyFix(application.wsgi_app)

    db.init_app(application)
    migrate.init_app(application, db)

    application.register_blueprint(services_v1)
    application.register_blueprint(views_v1)


    if not application.debug and not application.testing:

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        # stream_handler.setLevel(logging.DEBUG)
        application.logger.addHandler(stream_handler)

        application.logger.setLevel(logging.DEBUG)
        application.logger.info('Twitter management startup')

    return application
