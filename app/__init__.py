import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
login_manager.login_view = 'auth.do_the_login'
login_manager.session_protection = 'strong'

bcrypt = Bcrypt()

bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app(config_type): #dev, test, prod

    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config' , config_type + '.py')

    #add to current director + config + config_type + py

    app.config.from_pyfile(configuration)

    db.init_app(app) # bind database to flask

    bootstrap.init_app(app)

    login_manager.init_app(app)

    #bcrypt.init_app(bcrypt)

    from app.catalog import main #import blueprint

    app.register_blueprint(main) #register blueprint

    from app.auth import auth
    app.register_blueprint(auth)

    return app
