#!/usr/bin/python3
"""module for accessing JSONPlaceholder api"""


import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(id)
    )
    emp_tasks = response_todos.json()
    emp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(id)).json()

    tasks_list = []
    for task in emp_tasks:
        inner_dict = {
            "username": emp.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        }
        tasks_list.append(inner_dict)
    emp_jsonable = {id: tasks_list}
    with open('{}.json'.format(id), mode='w') as f:
        json.dump(emp_jsonable, f)
