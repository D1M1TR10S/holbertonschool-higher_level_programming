#!/bin/bash
# Sends a POST request to a URL and returns the body
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
