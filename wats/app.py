import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
db_location = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

db = SQLAlchemy(app)
Migrate(app, db)

db.init_app(app)

if __name__ == "__main__":
    from views import *
    app.run(debug=True)