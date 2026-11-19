from deepdiff import DeepDiff
import json
import sys
import os

"""
Used to compare differences between the original json and the modified json with readable human dates
(e.g., compares calendar.json to calendar_converted.json and email.json to email_converted.json).
"""

def compare_json_files(file1, file2):
    data1 = None
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)

    data2 = None
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    diff = DeepDiff(data1, data2)
    print(f"Differences between {file1} and {file2}:")
    print(diff)

if __name__ == "__main__":
    cal1 = 'calendar.json'
    cal2 = 'calendar_converted.json'

    email1 = 'email.json'
    email2 = 'email_converted.json'

    compare_json_files(cal1, cal2)
    compare_json_files(email1, email2)