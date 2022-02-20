from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = '601ehfiej4oe4mc1098a'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///login_user_information.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.config.from_object('config')

