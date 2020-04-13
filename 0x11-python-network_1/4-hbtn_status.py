#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status

from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    text_response = type(response.text)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(text_response))
    print("\t- content: {}".format(content))
