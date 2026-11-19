# outlier-auditing-tool-scripts
These are scripts I created to aid me in my work as a Quality Control auditor at Scale AI/Outlier. 

### Disclaimer
1. These are only for personal use and were made to improve my work and time efficiency. They aren't distributed throughout the company. 
1. There are no references made to the projects these scripts are used for, and the data the scripts require is dummy data to not represent company data.

## EDLParser Folder
This folder is for a project that required verifying edits within an EDL file. Some of the EDL files have numerous edits and are time-consuming to 
manually get the source and destination durations and verify the clips used. The parser computes the durations and checks if they match between them, and
they get the unique clips used. 

## GCalEmailJSONParser Folder
This folder is for a project that required verifying the accuracy of Google emails and calendar events (All provided JSONs contain dummy email and calendar content). 
Cross-checking the dates requires translation of Unix timestamps to human-readable dates and times (time based on the user's timezone). Numerous emails and calendar events
make this time-consuming. The parser translates these timestamps, appends the new timestamp to each email/calendar event and outputs them to a new JSONs with the previous content intact.
