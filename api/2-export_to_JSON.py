#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    users_url = main_url + "/users"
    todos_url = main_url + "/todos"

    users_result = requests.get(users_url).json()
    todos_result = requests.get(todos_url).json()

    json_dic = {}
    json_list = []

    for user in users_result:
        if user['id'] == int(argv[1]):
            user_name = user['username']
    for todo in todos_result:
        if todo['userId'] == int(argv[1]):
            internal_dict = {}
            internal_dict["task"] = todo['title']
            internal_dict["completed"] = todo['completed']
            internal_dict["username"] = user_name
            json_list.append(internal_dict)
    json_dic[argv[1]] = json_list
    with open(f"{argv[1]}.json", 'w') as json_file:
        json.dump(json_dic, json_file)
