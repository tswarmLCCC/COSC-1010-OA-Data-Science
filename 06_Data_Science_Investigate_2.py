# filename: 06_Data_Science_Investigate_2.py
"""
Activity: Investigate the Code

1.  This activity requires the file `books.csv`. Make sure it is in the same
    directory as this Python script.
2.  Run the code and observe the output of the `.shape` attribute.
3.  Answer the questions below in comments.

Questions:
1.  The output of `.shape` is a tuple with two numbers. What do you think the
    first number represents?
    # Your Answer Here

2.  What do you think the second number represents?
    # Your Answer Here

3.  How is this different from the `len()` function? Try adding `print(len(books_df))`
    to the code to find out.
    # Your Answer Here
"""

import pandas as pd

# This code assumes a file named books.csv exists with the following content:
# title,author,year
# The Hobbit,J.R.R. Tolkien,1937
# 1984,George Orwell,1949
# Dune,Frank Herbert,1965

# Load the data from the CSV file
books_df = pd.read_csv("books.csv")

# The .shape attribute tells you the dimensions of the DataFrame
dimensions = books_df.shape

print(f"The DataFrame has the shape: {dimensions}")
