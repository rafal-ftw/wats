from flask import render_template, request

from models import Scenario, create_scenario
from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/scenario_list", methods=["GET"])
def scenario_list():
    
    scenarios = Scenario.query.all()

    return render_template('scenario_list.html', scenarios = scenarios)

@app.route("/scenario_add", methods = ["GET", "POST"])
def add_scenario():
    if request.method == "GET":
        return render_template('add_scenario.html')
    
    scenario_name = request.form.get('name_field')
    scenario_expected = request.form.get('expected_field')
    """One text field for now, to be worked on"""
    scenario_steps = request.form.get('steps')
    scenario_author = request.form.get('author')
    scenario = create_scenario(scenario_name, scenario_expected, scenario_steps, scenario_author)

    return render_template('add_scenario.html', scenario = scenario)
# 
# @app.route("/scenario/<scenario_id>", methods = ["GET", "POST"])
# def single_scenario(scenario_id):
    # if request.method == "POST":
        # return f"get scenario {scenario_id} and update it!"
    # else:
        # return scenario_id