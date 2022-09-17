from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SECRET_KEY'] = 'testtesttest'

    from elasticapm.contrib.flask import ElasticAPM

    app.config['ELASTIC_APM'] = {
    # Set the required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    #'SERVICE_NAME': 'unknown-python-service',
    'SERVICE_NAME': 'brokurly',

    # Use if APM Server requires a secret token
    'SECRET_TOKEN': 'pRbQ84U8iPrAElKP3xiQmw',

    # Set the custom APM Server URL (default: http://localhost:8200)
    #'SERVER_URL': 'https://87aa10499be4400b8b0f6b0ba39ed7d8.apm.ap-northeast-2.aws.elastic-cloud.com:443',
    'SERVER_URL' : 'http://10.1.3.194:8200',

    # Set the service environment
    'ENVIRONMENT': 'production',
    }

    apm = ElasticAPM(app)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import register_views
    app.register_blueprint(register_views.bp)

    return app