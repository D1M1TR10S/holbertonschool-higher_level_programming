#!/usr/bin/python3
"""
Module that add arguments from command line to a list in a json file
"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
import sys


arg_list = []
try:
    arg_list = load_from_json_file('add_item.json')
except:
    pass
for a in range(len(sys.argv)):
    if a > 0:
        arg_list.append(sys.argv[a])
save_to_json_file(arg_list, 'add_item.json')
