from flask import Blueprint, flash, g, redirect, render_template, request, url_for



bp = Blueprint('views', __name__)



@bp.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@bp.route("/scenario_list", methods=["GET"])
def scenario_list():
    from basic import Scenario
    scenarios = Scenario.query.all()
    return render_template('scenario_list.html', scenarios = scenarios)

@bp.route("/scenario/add", methods = ["GET", "POST"])
def add_scenario():
    if request.method == "POST":
        return render_template('add_scenario_done.html')
    else:
        return render_template('add_scenario.html')

@bp.route("/scenario/<scenario_id>", methods = ["GET", "PUT", "POST"])
def single_scenario(scenario_id):
    if request.method == "PUT":
        return f"get scenario {scenario_id} and update it!"
    else:
        return scenario_id