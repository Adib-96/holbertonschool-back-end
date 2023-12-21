#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import requests
from sys import argv
from json import dump


def get_user_data():
    """Fetch user data from the API."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    return requests.get(users_url).json()


def get_todo_data():
    """Fetch todo data from the API."""
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    return requests.get(todos_url).json()


def export_data_to_json(users, todos, filename="todo_all_employees.json"):
    """Export data to JSON file."""
    nested_dict = {}

    for user in users:
        user_id = user["id"]
        user_name = user["username"]

        user_tasks = [
            {"task": task["title"],
             "completed": task["completed"], "username": user_name}
            for task in todos if task["userId"] == user_id
        ]

        nested_dict[user_id] = user_tasks

    with open(filename, "w") as f:
        dump(nested_dict, f, indent=2)


if __name__ == "__main__":
    users_data = get_user_data()
    todos_data = get_todo_data()

    export_data_to_json(users_data, todos_data)
