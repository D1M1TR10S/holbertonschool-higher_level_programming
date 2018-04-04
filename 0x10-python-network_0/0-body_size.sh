#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

curl -s --head $1 | grep "Content-Length" | sed 's/Content-Length: //'
