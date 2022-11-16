import os
import json
from app import *


class Scenario(db.Model):
    __tablename__ = 'scenarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    expected = db.Column(db.String(50))
    steps = db.Column(db.Text)
    author = db.String(db.String(255))

    def __init__(self, name, expected, steps, author):
        self.name = name
        self.expected = expected
        self.steps = steps
        self.author = author


def create_scenario(name, expected, steps, author):

    scenario = Scenario(name, expected, steps, author)
    db.session.add(scenario)
    db.session.commit()

    return scenario


class PossibleStep(db.Model):
    __tablename__ = 'possiblesteps'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    example_values = db.Column(db.Text)

    def __init__(self, name, type, description, example_values):
        self.name = name
        self.type = type
        self.description = description
        self.example_values = example_values


def create_possible_step(type, name, description, example_values):
    possible_step = PossibleStep(type, name, description, example_values)


def initiate_steps(data_path):

    with open(data_path) as json_file:
        data = json.load(json_file)

        print("Type: ", type(data))

        for category in data.keys():
            print("|__________________________________")
            print("|\n|\n|\n|TYPE:", category)
            print("|\n|\n|values:")
            for step in data[category]:
                print("|name: ", step)
                print("|values:", data[category][step]['values'])
                print("|description: %s \n|" % data[category][step]['description'])
            print("|\n|")

            # TODO MAP TO STEPS INTO THE DATABASE


if __name__ == "__main__":
    with app.app_context():
        print("Creating database tables..")
        # db.create_all()
        print("Done!")
        print("Loading initial data")
        initiate_steps(os.getcwd() + "/data/possiblesteps.json")
        print("Data initiation process finished, all possible steps loaded!")
