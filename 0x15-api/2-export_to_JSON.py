#!/usr/bin/python3

import requests
import json
import sys


def export_to_json(emp_num):

    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        emp_num)

    response = requests.get(url)
    response_json = response.json()
    username = response_json.get("username")
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        emp_num)
    res = requests.get(url2)
    res_json = res.json()

    tasks = []
    for i in res_json:
        task = {
            "task": i["title"],
            "completed": i["completed"],
            "username": username
            }
        tasks.append(task)
    out = {str(emp_num): tasks}

    file_name = "{}.json".format(emp_num)
    with open(file_name, "w") as f:
        json.dump(out, f)


if __name__ == "__main__":
    export_to_json(sys.argv[1])
