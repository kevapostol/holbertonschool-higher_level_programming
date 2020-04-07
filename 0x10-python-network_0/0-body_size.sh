#!/bin/bash
# a Bash script that takes in a URL and prints the bytes
curl --silent "$1" | wc -c
