#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    try:
        user_id = int(user_id)
    except ValueError:
        print("Error: User ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    try:
        user = requests.get(url + "users/{}".format(user_id)).json()
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
    except requests.RequestException as e:
        print("Error making API request:", e)
        sys.exit(1)

    if "id" not in user:
        print("Error: User not found.")
        sys.exit(1)

    username = user.get("username")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)

    print("Export successful. File saved as {}.json".format(user_id))
