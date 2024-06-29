import pandas as pd

data_path = "updated_dataset.csv"
data = pd.read_csv(data_path)

# Function to consolidate columns into a single column based on the first positive match
def consolidate_columns(row, columns):
    for col in columns:
        if row[col]:  # Assuming the presence is marked by a non-zero/non-null value
            return col.split('_')[-1]  # Return the last part of the column name
    return 'None'  # Return 'None' if no column matches

# Consolidate race columns
race_columns = [col for col in data.columns if col.startswith('race_ethnicity_')]
data['race'] = data.apply(consolidate_columns, columns=race_columns, axis=1)

# Consolidate texture columns
texture_columns = [col for col in data.columns if col.startswith('textures_')]
data['texture'] = data.apply(consolidate_columns, columns=texture_columns, axis=1)

# Consolidate condition symptoms columns
other_symptoms_columns = [col for col in data.columns if col.startswith('other_symptoms_')]
data['other_symptoms'] = data.apply(consolidate_columns, columns=other_symptoms_columns, axis=1)

# Consolidate condition symptoms columns
condition_columns = [col for col in data.columns if col.startswith('condition_symptoms_')]
data['conditions'] = data.apply(consolidate_columns, columns=condition_columns, axis=1)

# Drop the original columns now that we have consolidated them
data.drop(columns=race_columns + texture_columns + condition_columns + other_symptoms_columns, inplace=True)

# Remove rows without data entry or unknown age\
# data = data.dropna()
data = data[data['age_group'] != 'AGE_UNKNOWN']
data.drop(columns=['combined_race'], inplace=True)




# Return the updated dataset head
print("\nUpdated dataset head:")
print(data.head())
print(data.columns)

data.to_csv("new_dataset.csv", index=False)
print("\nUpdated dataset saved to new_dataset.csv")