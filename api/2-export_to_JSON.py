#!/usr/bin/python3
"""
Module to fetch user data and export their TODO list to a JSON file.
"""
import json
import requests
import sys


def get_user_info(user_id):
    """
    Retrieve user information by user ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()


def get_user_todos(user_id):
    """
    Retrieve the TODO list for the user by user ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    return response.json()


def save_todos_to_json(user_id, todos):
    """
    Save the TODO list to a JSON file.
    """
    filename = f"{user_id}.json"
    with open(filename, "w") as file:
        json.dump({user_id: todos}, file)


def main(user_id):
    """
    Main function to get user info and TODO list, then save to JSON.
    """
    user_info = get_user_info(user_id)
    todos_info = get_user_todos(user_id)

    username = user_info["username"]

    todos_list = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        } for task in todos_info
    ]

    save_todos_to_json(user_id, todos_list)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: ./2-export_to_JSON.py <user_id>")
