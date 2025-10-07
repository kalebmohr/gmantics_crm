"""
This is a sample application that does basically nothing excet read JSON data.
"""

import json

"""
This function opens a JSON file for reading.
It outputs contents to the terminal.
"""

def readJsonData(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data

print(readJsonData('data/example.json'))

