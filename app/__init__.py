from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/country"
app.config['JWT_SECRET_KEY'] = "Salima"
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth= HTTPBasicAuth()
jwt=JWTManager(app)


# Import CLI commands and controllers
from app import commands
from app.controllers import country_controllers
from app.controllers import user_controller