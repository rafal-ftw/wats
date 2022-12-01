from flask import render_template, request, Response

from models import Scenario, PossibleStep, create_scenario
from app import app
import pprint

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

@app.route("/scenario_added", methods = ["GET", "POST"])
def scenario_added():

    if request.method == "GET":
        return '<h6>bad request, it was get for /scenario_added</h6>' #TODO 404

    print(request.form.keys())
    print(request.form.items())
    scenario_data = request.form
    return render_template('scenario_added.html', data = scenario_data)

@app.route("/scenario_add_test", methods = ["GET", "POST"])
def scenario_add_test():

    data = request.get_json()
    
    print(data)
    for key in data:
        print(data[key])
    
    
    return 'redirected at test'
