from app import db


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


class Scenario(db.Model):
    __tablename__ = 'scenarios'
    id = db.Column(db.Integer, primary_key = True)
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


if __name__ == "__main__":
    print("Creating database tables..")
    db.create_all()
    print("Done!")