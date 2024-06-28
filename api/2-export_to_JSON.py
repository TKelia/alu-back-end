#!/usr/bin/python3
"""
Module to fetch user data and export their TODO list to a JSON file.
"""
import json
import requests
import sys


def fetch_user_info(user_id):
    """
    Retrieve user information by user ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()


def fetch_user_todos(user_id):
    """
    Retrieve the TODO list for the user by user ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    return response.json()


def save_to_json(user_id, todos):
    """
    Save the TODO list to a JSON file.
    """
    filename = f"{user_id}.json"
    with open(filename, "w") as file:
        json.dump({user_id: todos}, file)


def run(user_id):
    """
    Main function to get user info and TODO list, then save to JSON.
    """
    user_info = fetch_user_info(user_id)
    todos_info = fetch_user_todos(user_id)

    user_username = user_info["username"]

    todos_to_save = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_username
        } for task in todos_info
    ]

    save_to_json(user_id, todos_to_save)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Usage: ./2-export_to_JSON.py <user_id>")

