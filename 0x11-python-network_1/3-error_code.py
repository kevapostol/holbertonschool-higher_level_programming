#!/usr/bin/python3
# takes in a URL, sends a request to the URL
# and displays the body of the response

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import  URLError
req = Request(someurl)
try:
    response = urlopen(argv[1])
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    pass
