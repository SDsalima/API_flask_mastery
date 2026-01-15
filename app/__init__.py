from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/country"

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import CLI commands and controllers
from . import commands
from .controllers import country_controllers