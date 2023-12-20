#!/usr/bin/python3

"""
This module gather data from an API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    # Fetch TODO list for the given employee
    response = requests.get(todo_url)
    todos = response.json()

    # Fetch employee details
    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee = employee_response.json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Display progress
    print(f"Employee {employee['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
