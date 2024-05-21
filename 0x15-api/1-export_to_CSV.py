#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
his/her TODO list progress
"""

import csv
import json
import requests
import sys
from urllib.request import urlopen


def empreq(emp_num):
    """return employees todo"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        emp_num)

    response = requests.get(url)
    response_json = response.json()
    username = response_json.get("username")
    with urlopen("https://jsonplaceholder.typicode.com/todos?userId={}"
                 .format(emp_num)) as req:
        body = req.read()
        decode = body.decode("utf-8")
#        print(type(decode))
        res = json.loads(decode)
#        print(res)

        j = 0
#        print(res[1].items())
        with open("{}.csv".format(emp_num), "w", newline='') as f:
            wrt = csv.writer(f, quoting=csv.QUOTE_ALL)
            for i in res:
                row = [
                    emp_num,
                    username,
                    str(i["completed"]),
                    i["title"]
                    ]
                wrt.writerow(row)


if __name__ == "__main__":
    empreq(sys.argv[1])
