#!/usr/bin/python3
""" export data in the CSV format. """

import csv
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
    with open("{}.csv".format(employee_id), 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([
                employee_id,
                user.get('username'),
                task.get('completed'),
                task.get('title')
            ])
