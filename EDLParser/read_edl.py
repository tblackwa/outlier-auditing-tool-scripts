import sys
import os
from pathlib import Path
from datetime import datetime
from datetime import timedelta

"""
A parser used to read the an EDL file from DaVinci Resolve. It extracts the unique clip names made
in all of the edits. It also checks source duration and recorded duration of each video edit to see 
if they match (the audio edits are structurally the same as the video edits, so only one channel 
needs to be checked for the project context). If they don't match, it prints out the line in the 
EDL file that has the mismatch along with the source and recorded durations.

Usage: 
- The EDL file should be in the same folder with this script, and named "dummy.edl" 
- or to a different name. Change "dummy.edl" in the code (line 21) to the name of your EDL file. 
- Then run this script to see the results.
"""

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    edl_file = BASE_DIR / "EDLParser" / "dummy.edl"

    if os.path.exists(edl_file):
        # Read the EDL file and extract clip names and durations
        with open(edl_file, "r") as f:
            clip_names = []
            source_durs = []
            rec_durs = []
            lines = f.readlines()
            for line in lines:
                values = line.strip().split()
                if len(values) > 0:
                    # Parse lines that start with a number (these are the edit lines)
                    if values[0].startswith("0"):
                        # Parse the source and recorded durations for video edits
                        if values[2] == "V":
                            source_start = datetime.strptime(values[4], "%H:%M:%S:%f")
                            source_end = datetime.strptime(values[5], "%H:%M:%S:%f")
                            rec_start = datetime.strptime(values[6], "%H:%M:%S:%f")
                            rec_end = datetime.strptime(values[7], "%H:%M:%S:%f")

                            source_diff = source_end - source_start
                            rec_diff = rec_end - rec_start
                            source_durs.append(source_diff)
                            rec_durs.append(rec_diff)

                            if source_diff != rec_diff:
                                print(values)
                                print(f"Source Duration: {source_diff}, Recorded Duration: {rec_diff}, Durations Match: {source_diff == rec_diff}\n")

                    # Parse lines that start with an asterisk (these are the clip name lines)
                    if values[0].startswith("*"):
                        clip_names.append(values[-1])

            # Print the sums of the source and recorded durations, and the unique clip names
            print(f"Sum of Source Durations: {sum(source_durs, timedelta(0))}")
            print(f"Sum of Recorded Durations: {sum(rec_durs, timedelta(0))}")
            print(f"Unique Clip Names: {set(clip_names)}")

    else:
        sys.exit(f"EDL file not found at {edl_file}. Please make sure the file exists.")


