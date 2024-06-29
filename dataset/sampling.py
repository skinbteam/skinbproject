import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("new_dataset.csv")

# stratify by column
stratify_col = 'age_group' if 'age_group' in data.columns else None

if stratify_col:
    # Remove NaN
    data = data.dropna(subset=[stratify_col])
    
    # Split the data 
    _, data_subset = train_test_split(data, test_size=0.1, stratify=data[stratify_col], random_state=42)
else:
    # If no stratification column is applicable, take a random sample
    data_subset = data.sample(frac=0.1, random_state=42)

# Save 
data_subset.to_csv("subset_dataset.csv", index=False)
print("Subset saved to subset_dataset.csv")

print(data_subset.head())
print(data_subset.info())