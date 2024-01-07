import pandas as pd

# change the filename when applying to train/test 
filename = 'test_data_labels.csv'

df = pd.read_csv(filename)

# convert Cluster Labels from num to Categories 
# 0: Other/General Waste; 1: Plastic Waste; 2: Clothing/Textile Waste; 
# 3: E-waste; 4: Food Waste

# Assuming 'df' is a pandas DataFrame with a column named 'Cluster Labels' containing numerical labels
# We will map these numerical labels to their corresponding categories

# First, let's create a mapping dictionary for the cluster labels
cluster_mapping = {
    0: "Other/General Waste",
    1: "Plastic Waste",
    2: "Clothing/Textile Waste",
    3: "E-waste",
    4: "Food Waste"
}

# Now, apply the mapping to the 'Cluster Labels' column
df['Cluster Label'] = df['Cluster Label'].map(cluster_mapping)

# Show the DataFrame to confirm the changes
df.head()  # Display the first few rows to confirm the conversion
