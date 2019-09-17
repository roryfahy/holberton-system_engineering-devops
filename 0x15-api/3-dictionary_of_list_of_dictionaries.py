#!/usr/bin/python3
"""module for accessing JSONPlaceholder api"""


import json
import requests


if __name__ == '__main__':
    id_list = []
    emp_list = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    for user in emp_list:
        id_list.append(user.get('id'))
    id_list.sort()
    ret = {}
    for id in id_list:
        response_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(id)
        )
        emp = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(id)
        ).json()
        emp_tasks = response_todos.json()
        tasks_list = []
        for task in emp_tasks:
            inner_dict = {
                "username": emp.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(inner_dict)
        ret[id] = tasks_list
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(ret, f)
