from flask import render_template, request

from models import Scenario, PossibleStep, create_scenario
from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/scenario_list", methods=["GET"])
def scenario_list():
    
    scenarios = Scenario.query.all()

    return render_template('scenario_list.html', scenarios = scenarios)

@app.route("/scenario_add", methods = ["GET", "POST"])
def scenario_add():

    steps = PossibleStep.query.all()

    step_names = []
    for i in steps:
        step_names.append(i.name)
    

    if request.method == "GET":
        return render_template('scenario_add.html', steps = steps)

     
    scenario_name = request.form.get('name_field')
    scenario_expected = request.form.get('expected_field')
    scenario_author = request.form.get('author')
    
    scenario_details = [scenario_name, scenario_expected, scenario_author]

    return render_template('add_steps.html', scenario_details = scenario_details, step_names = step_names)

@app.route("/add_steps", methods = ["GET", "POST"])
def add_steps(scenario_details = None):

    steps = PossibleStep.query.all()
    
    step_names = []
    for i in steps:
        step_names.append(i.name)
    
    if request.method == "GET":
        return (render_template('scenario_list.html')) #TODO 404

    if request.method == "POST" and len(scenario_details) == 3:
        return render_template('add_steps.html', scenario_details = scenario_details, step_names = step_names)
    