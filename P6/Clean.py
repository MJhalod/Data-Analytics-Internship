import pandas as pd

# Load the dataset
df = pd.read_csv('ecommerce_furniture_dataset_2024.csv')
# Remove '$' and ',' characters
# The 'regex=True' part allows us to remove multiple characters at once
df['price'] = df['price'].astype(str).str.replace(r'[$,]', '', regex=True)

# Convert the cleaned column to a numeric (float) type
df['price'] = pd.to_numeric(df['price'])
# Remove '$' and ',' characters
df['originalPrice'] = df['originalPrice'].astype(str).str.replace(r'[$,]', '', regex=True)

# Convert to numeric.
# 'errors='coerce'' is important: it automatically turns any errors
# (like blank cells or 'nan' text) into a proper NaN (Not a Number) value.
df['originalPrice'] = pd.to_numeric(df['originalPrice'], errors='coerce')
# Fill any missing values in 'tagText' with the string 'Unknown'
df['tagText'] = df['tagText'].fillna('Unknown')
# 1. Calculate Total Revenue
df['Total_Revenue'] = df['price'] * df['sold']

# 2. Calculate the Discount Amount
df['Discount_Amount'] = df['originalPrice'] - df['price']

# 3. Calculate the Discount Percentage
df['Discount_Percentage'] = (df['originalPrice'] - df['price']) / df['originalPrice']

# Fill any resulting NaNs with 0 (for items with no originalPrice)
df['Discount_Percentage'] = df['Discount_Percentage'].fillna(0)
# Save the cleaned and enhanced data to a new file
df.to_csv('cleaned_ecommerce_furniture.csv', index=False)