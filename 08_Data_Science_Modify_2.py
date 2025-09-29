# filename: 08_Data_Science_Modify_2.py
"""
Activity: Modify the Code

This program filters a DataFrame to show all employees who are in the
'Sales' department.

Your goal:
1.  Modify the filtering condition to instead show all employees who have a
    salary **greater than 70000**.
"""

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['Engineering', 'Sales', 'Engineering', 'Marketing'],
    'salary': [90000, 65000, 95000, 72000]
}
employees_df = pd.DataFrame(data)

# --- MODIFY THE LINE BELOW ---
# Change the condition inside the square brackets
filtered_df = employees_df[employees_df['department'] == 'Sales']
# --- END MODIFICATION ---

print("Filtered Employees:")
print(filtered_df)
