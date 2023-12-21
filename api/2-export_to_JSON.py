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
    user_id = argv[1]
    json_file = f"{user_id}.json"

    req_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    req_todo = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_id))

    username_value = req_name.json()['username']
    user_data = req_todo.json()

    my_array = []
    for el in user_data:
        my_array.append({"task": "{}".format(el['title']),
                         "completed": "{}".format(
            el['completed']), "username": "{}".format(username_value)})
    format_ready_for_json = json.dumps({"{}".format(user_id): my_array})
    with open(json_file, "w") as js_f:
        js_f.write(format_ready_for_json)


exportJson()
