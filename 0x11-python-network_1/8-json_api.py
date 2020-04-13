#!/usr/bin/python3
"""
a Python script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user with the
letter as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        val = ""
    else:
        val = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': val})
    deserialized_json = response.json()

    if response.request.headers['Content-Type'] != 'application/json':
        print("Not a valid JSON")
    elif len(deserialized_json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(deserialized_json.get("id"),
                               deserialized_json.get("name")))
