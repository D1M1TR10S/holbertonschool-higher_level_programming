#!/bin/bash
# Sends a POST request to a URL and returns the body
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
