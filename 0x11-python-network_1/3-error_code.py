#!/usr/bin/python3
# takes in a URL, sends a request to the URL
# and displays the body of the response

from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
