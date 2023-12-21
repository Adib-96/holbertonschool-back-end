#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import requests
from sys import argv


def export_to_CSV():
    """
    function deal with api
    """
    user_id = argv[1]
    req_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    req_todo = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_id))

    result = req_todo.json()
    username = (req_name.json()['username'])
    csv_file = f"{user_id}.csv"

    with open(csv_file, 'w') as f:
        for ele in result:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    user_id,
                    username,
                    ele['completed'],
                    ele['title']))


if __name__ == "__main__":
    export_to_CSV()
