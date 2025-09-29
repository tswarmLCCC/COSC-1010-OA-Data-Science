# filename: 04_Data_Science_Predict_2.py
"""
Activity: Predict the Output

1.  Read the code below. It creates a DataFrame of student test scores.
2.  The code then filters the DataFrame to find only the rows where the score is greater than 90.
3.  Without running the code, predict what the final printed output will be.
"""

import pandas as pd

prediction = "" # What will the filtered DataFrame look like?

data = {
    'student': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 92, 95, 88]
}

scores_df = pd.DataFrame(data)

# This is a filtering condition. It creates a new DataFrame
# containing only the rows that meet the condition.
high_scores = scores_df[scores_df['score'] > 90]

print(high_scores)
