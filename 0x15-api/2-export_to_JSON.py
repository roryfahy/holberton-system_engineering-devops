#!/usr/bin/python3
"""module for accessing JSONPlaceholder api"""


import csv
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(id)
    )
    emp_tasks = response.json()
    USERNAME = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(id)).json().get('username')
    with open('{}.csv'.format(id), mode='w') as f:
        f_writer = csv.writer(
            f, delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )
        for todo_dict in emp_tasks:
            f_writer.writerow(
                [
                    id, USERNAME,
                    todo_dict.get('completed'),
                    todo_dict.get('title')
                ]
            )
