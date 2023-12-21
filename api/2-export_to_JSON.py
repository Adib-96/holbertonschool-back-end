#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import requests
from sys import argv
from json import dump

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    try:
        req_employee = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        req_employee.raise_for_status()

        req_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        req_todo.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit(1)

    username = req_employee.json()["username"]
    todos = req_todo.json()

    filename = f"{employee_id}.json"
    data = {employee_id: [{"task": todo["title"],
                           "completed": todo["completed"],
                           "username": username} for todo in todos]}

    with open(filename, "w") as f:
        dump(data, f, indent=2)
