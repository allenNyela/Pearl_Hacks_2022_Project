from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
#from cockroachdb.sqlalchemy import run_transaction

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = '601ehfiej4oe4mc1098a'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///login_user_information.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config.from_object('config')
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

#holds all database-related code
from app import db
from werkzeug.security import check_password_hash, generate_password_hash


#Table of all users and their related info
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    phone_number = db.Column(db.String(12), unique=True, nullable=False)
    birthMonth = db.Column(db.String(2), nullable=True)
    birthDay = db.Column(db.String(2), nullable=True)
    birthYear = db.Column(db.String(4), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    age = db.Column(db.String(3), nullable=True)
    state = db.Column(db.String(15), nullable=True)
    foods = db.Column(db.String(200), nullable=True)
    password_hash = db.Column(db.String(128))

    #sets user's password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)