#!/usr/bin/python3
""" export data in json formaat"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users/{}"
    user_url = base_url.format(employee_id)
    todos_url = base_url.format(employee_id) + "/todos"
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user = response.json()
    todos = requests.get(todos_url).json()
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open("{}.json".format(employee_id), 'w') as json_file:
        json.dump({employee_id: tasks_list}, json_file)
