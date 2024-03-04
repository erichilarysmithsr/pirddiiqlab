import pandas as pd
import numpy as np

# Read the food label data into a Pandas DataFrame
df = pd.read_csv('food_labels.csv')

# Extract the relevant information from the food label data
# In this example, we are extracting the following information:
# - The name of the food product
# - The serving size
# - The calories per serving
# - The fat content per serving
# - The sodium content per serving
# - The carbohydrate content per serving
# - The protein content per serving

df = df[['name', 'serving_size', 'calories', 'fat', 'sodium', 'carbohydrates', 'protein']]

# Format the extracted information in a way that is easy to understand
# In this example, we are formatting the information as follows:
# - The name of the food product is formatted as a title
# - The serving size is formatted as a number with two decimal places
# - The calories per serving, fat content per serving, sodium content per serving, carbohydrate content per serving, and protein content per serving are all formatted as numbers with one decimal place

df['name'] = df['name'].str.title()
df['serving_size'] = df['serving_size'].astype('float').round(2)
df['calories'] = df['calories'].astype('float').round(1)
df['fat'] = df['fat'].astype('float').round(1)
df['sodium'] = df['sodium'].astype('float').round(1)
df['carbohydrates'] = df['carbohydrates'].astype('float').round(1)
df['protein'] = df['protein'].astype('float').round(1)

# Save the formatted information to a file
df.to_csv('food_labels_formatted.csv', index=False)
