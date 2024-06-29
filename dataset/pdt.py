
import pandas as pd
import numpy as np

data_path = "dataset_scin_cases.csv"
data = pd.read_csv(data_path)

# List all the columns in the dataset
print("Columns in the dataset:")
print(data.columns)

# Remove columns with specific names
columns_to_drop = ["source", "release", "year", "body_parts_arm", "body_parts_palm", "body_parts_back_of_hand", "body_parts_torso_front", "body_parts_torso_back", "body_parts_genitalia_or_groin", "body_parts_buttocks", "body_parts_leg", "body_parts_foot_top_or_side","body_parts_foot_sole", "body_parts_other", "other_symptoms_joint_pain", "related_category"]  
data = data.drop(columns=columns_to_drop)

# Return the updated dataset head
print("\nUpdated dataset head:")
print(data.head())
print(data.columns)

data.to_csv("updated_dataset.csv", index=False)
print(f"\nUpdated dataset saved to updated_dataset.csv")