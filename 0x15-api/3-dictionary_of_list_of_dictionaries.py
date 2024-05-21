#!/usr/bin/python3
"""exports all tasks and users into a file"""
import requests
import json
import sys


def all_user():
    """returns user json"""
    user_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(user_url)
    return(response.json())


def all_todos():
    """returns all json todo"""
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    res = requests.get(tasks_url)
    return(res.json())


def export_all_to_json():
    """exports all tasks and users into a file"""
    users = all_user()
    todos = all_todos()

    user_dict = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_dict[user_id] = username

    tasks_dict = {}
    for i in todos:
        user_id = i["userId"]
        if user_id not in tasks_dict:
            tasks_dict[user_id] = []
        task = {
            "username": user_dict[user_id],
            "task": i["title"],
            "completed": i["completed"]
        }
        tasks_dict[user_id].append(task)

#    out = {str(emp_num): tasks}

    json_f = "todo_all_employees.json"

    with open(json_f, "w") as f:
        json.dump(tasks_dict, f)


if __name__ == "__main__":
    export_all_to_json()
