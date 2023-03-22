import pandas as pd

# Load your Excel file into a pandas DataFrame
df = pd.read_csv('D:/Downloads/Book1.csv')

# Group by book title and concatenate the authors' names
df_grouped = df.groupby(['ASIN', 'title'])['author'].apply(lambda x: ', '.join(x)).reset_index()

# Write the grouped data back to Excel
df_grouped.to_csv('Bookmerged.csv', index=False) # to change encoding='utf-8'