#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
his/her TODO list progress
"""

from urllib.request import urlopen
import sys
import json
import requests


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
        num_completed = 0
        for i in res:
            if res[j].get("completed") is True:
                num_completed += 1
            j += 1

        print("Employee {} is done with tasks ({}/{}):".format(
            username, num_completed, len(res)))

        k = 0
        for itm in res:
            if res[k].get("completed") is True:
                print("\t{}".format(res[k].get("title")))
            k += 1


if __name__ == "__main__":
    empreq(sys.argv[1])
