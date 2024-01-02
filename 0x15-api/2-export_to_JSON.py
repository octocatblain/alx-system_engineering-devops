#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()

    if "id" not in user_data:
        print("Error: User not found.")
        sys.exit(1)

    username = user_data.get("username")

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos_data = todos_response.json()

    user_tasks = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos_data
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(user_tasks, jsonfile)

    print("JSON file exported successfully for USER_ID: {}".format(user_id))
