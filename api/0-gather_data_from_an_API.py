#!/usr/bin/python3
"""
Python script to display the TODO list progress for a given employee ID.
"""
import requests
import sys


def fetch_employee_details(emp_id):
    """
    Retrieve employee details using employee ID.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/'
    response = requests.get(url)
    return response.json()


def fetch_employee_todos(emp_id):
    """
    Retrieve TODO list of the employee using employee ID.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    response = requests.get(url)
    return response.json()


def display_todo_progress(emp_id):
    """
    Display the TODO list progress of the employee.
    """
    employee = fetch_employee_details(emp_id)
    employee_name = employee.get("name")

    todos = fetch_employee_todos(emp_id)
    todo_status = {todo.get("title"): todo.get("completed") for todo in todos}

    total_tasks = len(todo_status)
    completed_tasks = [status for status in todo_status.values() if status]
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} has completed"
          f"({completed_count}/{total_tasks}) tasks:")
    for title, completed in todo_status.items():
        if completed:
            print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        display_todo_progress(sys.argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
