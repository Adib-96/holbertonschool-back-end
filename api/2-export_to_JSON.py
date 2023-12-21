#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
from sys import argv
import json
import requests


def exportJson():
    """
    function that use an api to format datas
    """
    employee_id = argv[1]
    req_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    req_employee = req_employee.json()
    username = req_employee["username"]
    req_todo = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id))
    req_todo = req_todo.json()
    filename = "{}.json".format(employee_id)
    nested_dic = {}
    my_list = []
    
    for i in req_todo:
        dict = {
            "task": i["title"],
            "completed": i["completed"],
            "username": username}
        my_list.append(dict)
    nested_dic[employee_id] = my_list
    with open(filename, "w") as f:
        json.dump(nested_dic, f)


if __name__ == "__main__":
    exportJson()
