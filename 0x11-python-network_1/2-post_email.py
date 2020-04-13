#!/usr/bin/python3
# a Python script that takes in a URL and an email,
# sends a POST request to the passed URL with the
# email as a parameter, and displays the body of the response
import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode("utf-8"))
