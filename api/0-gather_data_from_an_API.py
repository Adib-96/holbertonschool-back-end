#!/usr/bin/python3
"""
Python script that, use a REST API .
"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """
    function that fetch ressources from an endpoint
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    # Get user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    # Construct the result string
    result_string = (
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_number_of_tasks}):\n"
    )

    for task in completed_tasks:
        result_string += f"\t{task['title']}\n"

    return result_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    result = get_employee_todo_list(employee_id)
    sys.stdout.write(result)
