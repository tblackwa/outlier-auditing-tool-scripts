"""
Author: Tyler Blackwater
Date of Creation: 10/08/2026

This script is for Google Calendar and Email jsons for a project.

This script converts timestamps in calendar.json and email.json files in 
the current folder this script/executable is running in. This is turned 
into a human-readable format and saves the modified data to new JSON files
(calendar_converted.json and email_converted.json) in the current folder.
"""

import sys
import os
import json
from datetime import datetime

def convert_calendar_timestamps():
    # Get json data from calendar.json and check if no errors occurred
    data = None
    with open('calendar.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data is None:
        print("No data found in calendar.json or an error occurred.")

    # Copy and write calendar events to new dict with converted timestamps
    mod_data = {'events': []}
    for event in data['events']:
        # Go through each field in current cal event
        cur_event = {}
        for field, values in event.items():
            # Write fields to new dict's event, including the converted timestamps
            cur_event[field] = values
            if 'start_datetime' == field:
                cur_event['start_date_wtime'] = datetime.fromtimestamp(values).strftime('%m-%d-%Y %I:%M:%S %p')
            elif 'end_datetime' == field:
                cur_event['end_date_wtime'] = datetime.fromtimestamp(values).strftime('%m-%d-%Y %I:%M:%S %p')

        # Append the current event to the new dict's events list
        mod_data['events'].append(cur_event)

    # Write the new dict to a new json file in the current folder
    with open('calendar_converted.json', 'w', encoding='utf-8') as f:
        json.dump(mod_data, f, ensure_ascii=False, indent=2)

def convert_email_timestamps():
    # Get json data from email.json and check if no errors occurred
    data = None
    with open('email.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data is None:
        print("No data found in email.json or an error occurred.")

    # Copy and write emails to new dict with converted timestamps
    mod_data = {'emails': []}
    for event in data['emails']:
        # Go through each field in current email
        cur_event = {}
        for field, values in event.items():
            # Write fields to new dict's email, including the converted timestamp
            cur_event[field] = values
            if 'timestamp' == field:
                cur_event['date'] = datetime.fromtimestamp(values).strftime('%m-%d-%Y %I:%M:%S %p')

        # Append the current email to the new dict's emails list
        mod_data['emails'].append(cur_event)

    # Write the new dict to a new json file in the current folder
    with open('email_converted.json', 'w', encoding='utf-8') as f:
        json.dump(mod_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Get the list of files in current folder and check for JSON files
    current_dir_files = os.listdir(os.getcwd())
    jsons = [file for file in current_dir_files if file.endswith('.json')]
    if jsons == []:
        print("No JSON files found in the current folder.")
        sys.exit(1)
    if 'calendar.json' not in jsons and 'email.json' not in jsons:
        print("No calendar.json or email.json files found in the current folder.")
        sys.exit(1)

    # If calendar.json exists, convert the timestamps
    if 'calendar.json' in jsons:
        convert_calendar_timestamps()

    # If email.json exists, convert the timestamps
    if 'email.json' in jsons:
        convert_email_timestamps()