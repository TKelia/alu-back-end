#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""
import json
import requests


def fetch_all_users():
    """
    Retrieve the list of all users.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def fetch_user_todos(user_id):
    """
    Retrieve the TODO list for a given user ID.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def save_all_todos_to_json(users):
    """
    Save all users' TODO lists to a JSON file.
    """
    all_todos = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in fetch_user_todos(user["id"])
        ] for user in users
    }
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos, jsonfile)


def main():
    """
    Main function to fetch users and their TODO lists, then save to JSON.
    """
    users = fetch_all_users()
    save_all_todos_to_json(users)


if __name__ == "__main__":
    main()

