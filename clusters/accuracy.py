import pandas as pd

data_difference = pd.read_csv('test_data_labels_manual_labels.csv') 

# Count how many values are different between 'Cluster Label' and 'Manual Label'
difference_count = (data['Cluster Label'] != data['Manual Label']).sum()
difference_count
