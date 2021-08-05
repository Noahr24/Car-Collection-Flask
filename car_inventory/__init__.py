from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from config import Config
from flask_migrate import Migrate
from .models import db, login_manager

app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(site)
app.register_blueprint(auth)

db.init_app(app)

migrate = Migrate(app, db)
login_manager.init_app(app)

login_manager.login_view = 'signin'

from .models import User