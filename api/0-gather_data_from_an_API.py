#!/usr/bin/python3
"""Python script that, use a REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import requests
from sys import argv
if __name__ == "__main__":
    employee_id = argv[1]
    req_user_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    req_name = req_user_name.json()
    name = req_name["name"]
    req_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )
    req_todo = req_todo.json()
    completed_tasks = 0
    for i in req_todo:
        if i["completed"]:
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed_tasks,
                                                          len(req_todo)))
    for i in req_todo:
        if i["completed"]:
            print("\t {}".format(i["title"]))