# filename: 05_Data_Science_Investigate_1.py
"""
Activity: Investigate the Code

1.  This activity requires the file `temps.csv`. Make sure it is in the same
    directory as this Python script.
2.  Run the code and observe the output of the `.describe()` method.
3.  Answer the questions below in comments.

Questions:
1.  What does the 'count' row tell you about the 'temp_celsius' and 'humidity' columns?
    # Your Answer Here

2.  What does the 'mean' row represent?
    # Your Answer Here

3.  Look at the 'min' and 'max' rows for the 'temp_celsius' column. What was the lowest and highest temperature recorded?
    # Your Answer Here
"""

import pandas as pd

# This code assumes a file named temps.csv exists with the following content:
# day,temp_celsius,humidity
# 1,22,60
# 2,25,55
# 3,24,58
# 4,26,53
# 5,23,61

# Load the data from the CSV file
weather_df = pd.read_csv("temps.csv")

# The .describe() method gives you a statistical summary of the numerical columns
summary = weather_df.describe()

print("Statistical Summary:")
print(summary)
