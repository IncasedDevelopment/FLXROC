import os, sys
from flask import Flask

# import configs
from flxroc.config import ProdConfig, TestConfig

# login manager
from flask_login import LoginManager

# import models and create tables in database
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# server and client generator
from flxroc import client, server
_debug = bool('--debug' in sys.argv)
c2 = server.C2(debug=_debug)

def create_app(test=False):
    # initialize app and configure global objects
    app = Flask(__name__,
                static_url_path='/assets', 
                static_folder='assets',
                template_folder='templates')

    # configure app
    config = ProdConfig if not test else TestConfig
    app.config.from_object(config)

    from flxroc.models import db, bcrypt
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        bcrypt.init_app(app)
        login_manager.init_app(app)

        # import blueprints
        from flxroc.main.routes import main
        from flxroc.users.routes import users
        from flxroc.api.files.routes import files
        from flxroc.api.session.routes import session
        from flxroc.api.payload.routes import payload
        from flxroc.errors.handlers import errors

        # register blueprints
        app.register_blueprint(main)
        app.register_blueprint(users)
        app.register_blueprint(files)
        app.register_blueprint(session)
        app.register_blueprint(payload)
        app.register_blueprint(errors)

        # bind app to server
        c2.bind_app(app)
        
        return app
