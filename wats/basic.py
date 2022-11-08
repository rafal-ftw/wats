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

with app.app_context():
    db.create_all()


from views import bp
app.register_blueprint(bp)


class PossibleStep(db.Model):
    __tablename__ = 'possiblesteps'
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(50))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)

    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

    def __repr__(self):
        return 'Step #%s,\ntype: %s,\nname: %s\n,desc: %s' % self.id, self.type, self.name, self.description

class Scenario(db.Model):
    __tablename__ = 'scenarios'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    expected = db.Column(db.String(50))
    steps = db.Column(db.Text)

    def __init__(self, name, expected, steps):
        self.name = name
        self.expected = expected
        self.steps = steps

    def __repr__(self):
        return 'Scenario #%s,\nExpected outcome: %s,\nsteps:%s' % self.name, self.expected, self.steps