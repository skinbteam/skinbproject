
import pandas as pd
import numpy as np

data_path = "updated_dataset.csv"
data = pd.read_csv(data_path)

# List all the columns in the dataset
print("Columns in the dataset:")
print(data.columns)

# Remove rows without data entry or unknown age 
# data = data.dropna()

data = data[data['age_group'] != 'AGE_UNKNOWN']

# Return the updated dataset head
print("\nUpdated dataset head:")
print(data.head())
print(data.columns)

data.to_csv("new_dataset.csv", index=False)
print(f"\nUpdated dataset saved to new_dataset.csv")