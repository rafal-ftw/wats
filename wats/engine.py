from datetime import datetime

from models import *


def start_execution(Execution):
    print("Execution started, ", Execution)
    
    log_to_execution(Execution, "Execution started!")

    print(Execution.logs)
