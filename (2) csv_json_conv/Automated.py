import csv
import json

DEFAULT_INPUT_FILE_NAME = 'input.csv'
DEFAULT_OUTPUT_FILE_NAME = 'output.json'

with open(DEFAULT_INPUT_FILE_NAME, "r") as csvfile:
    data = list(csv.DictReader(csvfile))

with open(DEFAULT_OUTPUT_FILE_NAME, "w") as jsonfile:
    json.dump(data, jsonfile)

