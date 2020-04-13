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

    try:
        url = "http://0.0.0.0:5000/search_user"
        response = requests.post(url, data={'q': val})
        deserialized_json = response.json()

        if "id" in deserialized_json and "name" in deserialized_json:
            print("[{}] {}".format(deserialized_json.get("id"),
                                   deserialized_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
