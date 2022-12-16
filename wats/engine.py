import json
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from models import *




class Test:
    def __init__(self, Execution):
        self.Execution = Execution
        self.steps = Execution.steps
        self.flag = False
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def kill_driver(self):
        self.driver.quit()

    def interpret_steps(self):
        self.steps = self.steps.replace('\'', '"')

        print(self.steps)
        steps = json.loads((self.steps.replace('\'', '\"')))
        
        for step in steps:
            print(steps[step])

            function = steps[step]['function']
            # print(function)
            values = steps[step]['values']
            # print(values)
            run_action(self, function, values)
        
        if self.flag == True:
            print('steps have been interpreted, the test has been successfull')
        else:
            print('steps have been interpreted, the test has been unsuccessfull')

        # sleep(5)


def run_action(test, function, values):
    match function:

        case "go_to_url":
            url = values['url']
            
            test.driver.get(url)

        case "click_element":
            xpath = values['xpath']
            try:
                test.driver.find_element(By.XPATH, xpath).click()
            except Exception as e:
                print(e)

        case "send_keys_to_element":
            xpath = values['xpath']
            send_value = values['keysToSend']
            try:
                test.driver.find_element(By.XPATH, xpath).send_keys(send_value)
            except Exception as e:
                print(e)

        case "wait":
            try:
                time_amount = int(values['amount'])
                sleep(time_amount)
            except:
                print("time is not int type, skipping waiting")
    

        case "assert_element_contains_string":
            xpath = values['xpath']
            string = values['string']

            try:
                elem = test.driver.find_elements(By.XPATH, xpath)

                if elem.value == string:
                    print(f"Element located at {xpath} contains string {string}")
                    test.flag = True
                else:
                    test.flag = False

            except Exception as e:
                print(e)

        case "assert_title_is":
            string = values['string']

            try:
                title = test.driver.title

                if title == string:
                    print(f"title is {string}")
                    test.flag = True
                else:
                    test.flag = False
            except Exception as e:
                print(e)

        
        case "assert_title_has":
            string = values['string']

            try:
                title = test.driver.title

                if string in title:
                    print(f"title is {string}")
                    test.flag = True
                else:
                    test.flag = False
            except Exception as e:
                print(e)

        case "assert_string_exists":
            source = test.driver.page_source

            string = values['string']
            try:
                if string in source:
                    print(f"source contains string {string}")
                    test.flag = True
                else:
                    test.flag = False
            except Exception as e:
                print(e)


        case _:
            print("there has been an error in step function parsing!")



def start_execution(Execution):
    print("====================\nExecution started\nInitiating Test Class")

    flag = False
    
    current = Test(Execution)
    log_to_execution(Execution, "Execution started!")

    log_to_execution(Execution, f"Steps to interpretation {current.steps}")
    current.interpret_steps()


    current.kill_driver()
