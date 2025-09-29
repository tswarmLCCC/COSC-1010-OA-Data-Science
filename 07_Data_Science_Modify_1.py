# filename: 07_Data_Science_Modify_1.py
"""
Activity: Modify the Code

This program loads a DataFrame of product prices and calculates the average
(mean) price.

Your goal:
1.  Modify the code to find the **highest** price instead of the average price.
2.  You will need to use a different pandas method. (Hint: think "maximum")
"""

import pandas as pd

data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price_usd': [1200, 25, 75, 300]
}
products_df = pd.DataFrame(data)

# --- MODIFY THE LINE BELOW ---
# Change .mean() to the method that finds the highest value
average_price = products_df['price_usd'].mean()
# --- END MODIFICATION ---

print(f"The result is: {average_price}")
