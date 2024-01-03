#!/usr/bin/python3
"""
Fetch and Export to JSON employee TODO list progress using a REST API.
"""
import json
import requests
import sys


def export_to_json():
    """return API data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(base_url + f"users/{user_id}").json()
    todos = requests.get(base_url + f"users/{user_id}/todos").json()

    """Export data to JSON"""
    with open(f"{user_id}.json", 'w') as jsonfile:
        json.dump({user_id: [{
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        }for todo in todos]}, jsonfile)


if __name__ == '__main__':
    export_to_json()
