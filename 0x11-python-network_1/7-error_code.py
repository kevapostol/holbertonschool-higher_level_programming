#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a
request to the URL and displays the body of 
the response
"""

import requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        print(response.text)
        response.raise_for_status()
    except HTTPError as http_err:
        print("Error code: {}".format(http_err))
