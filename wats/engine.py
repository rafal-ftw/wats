from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from models import *




class Test:
    def __init__(self, Execution):
        self.Execution = Execution
        self.steps = Execution.steps

    def initiate_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def interpret_steps(self):
        steps = self.steps
        
        for step in steps:
            print(step)

        sleep(5)



    def kill_driver(self):
        self.driver.quit()

def start_execution(Execution):
    print("====================\nExecution started\nInitiating Test Class")

    
    current = Test(Execution)
    
    
    log_to_execution(Execution, "Execution started!")
    current.initiate_driver()
    log_to_execution(Execution, f"Steps to interpretation {current.steps}")
    current.interpret_steps()

    current.kill_driver()



    print(Execution.logs)


