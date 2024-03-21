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
    for user in users_result:
        user_id = user['id']

        if user_id not in json_dic:
            json_dic[user_id] = []

        for todo in todos_result:
            internal_dic = {}
            if user_id == todo['userId']:
                internal_dic["username"] = user['username']
                internal_dic["task"] = todo['title']
                internal_dic["completed"] = todo['completed']
                json_dic[user_id].append(internal_dic)

    with open(f"todo_all_employees.json", 'w') as j_file:
        json.dump(json_dic, j_file)
