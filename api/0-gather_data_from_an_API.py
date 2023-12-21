#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    try:
        # Fetch user information
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        name = user_data["name"]

        # Fetch user's TODO list
        todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        # Count completed tasks and print information
        completed_tasks = sum(1 for todo in todo_data if todo["completed"])
        print("Employee {} is done with tasks ({}/{}):".format(name, completed_tasks, len(todo_data)))

        # Print completed task titles
        for todo in (todo for todo in todo_data if todo["completed"]):
            print("\t{}".format(todo["title"]))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit(1)
