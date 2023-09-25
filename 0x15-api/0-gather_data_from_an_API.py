#!/usr/bin/env python3
""" returns information about his/her TODO list"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user = response.json()
    todos = requests.get(todos_url).json()
    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(user['name'], len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task['title']))
