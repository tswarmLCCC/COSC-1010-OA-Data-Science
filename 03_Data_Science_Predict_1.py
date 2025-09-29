# filename: 03_Data_Science_Predict_1.py
"""
Activity: Predict the Output

1.  Read the code below. It uses the pandas library to create a DataFrame.
2.  A DataFrame is like a table. This one has two columns: 'fruit' and 'quantity'.
3.  The code then selects the 'fruit' column.
4.  Without running the code, what do you think the output of the print statement will be?
5.  Write your prediction in the `prediction` variable.
"""

import pandas as pd

prediction = "" # What will be printed?

data = {
    'fruit': ['apple', 'orange', 'banana'],
    'quantity': [5, 3, 10]
}

# Create a DataFrame from the dictionary
inventory_df = pd.DataFrame(data)

# Select just the 'fruit' column
fruits = inventory_df['fruit']

print(fruits)
