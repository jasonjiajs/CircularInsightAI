# # Load the CSV data
# csv_file_path = 'full_dataset.csv'
# data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

# ############### STEP 1 Split DATA ####################
# Split the data into train and test sets
train_data, test_data = train_test_split(data, test_size=100, random_state=42)
# Save train and test sets to new CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('validation_and_test_data.csv', index=False)
