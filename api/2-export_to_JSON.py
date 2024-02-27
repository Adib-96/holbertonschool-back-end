#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import requests
from sys import argv
from json import dump
if __name__ == "__main__":
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
    l = []
    for i in req_todo:
        dict = {
            "task": i["title"],
            "completed": i["completed"],
            "username": username}
        l.append(dict)
    nested_dic[employee_id] = l
    with open(filename, "w") as f:
        dump(nested_dic, f)
