import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pickle

def categories(file_obj):
    
    test_data = pd.read_csv(file_obj)


    # Load the kmeans model
    with open('kmeans.pkl', 'rb') as file:
        kmeans = pickle.load(file)

    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    
    # Pre-processing the test data (assuming it needs similar processing as problem_statements)
    

    test_problem_statements = test_data['problem'].dropna().values

    # Vectorizing the test data using the same vectorizer
    X_test = vectorizer.transform(test_problem_statements)

    # Predicting the cluster labels for the test data
    test_clusters = kmeans.predict(X_test)

    test_data['Cluster Label'] = test_clusters

    cluster_mapping = {
    0: "Other/General Waste",
    1: "Plastic Waste",
    2: "Clothing/Textile Waste",
    3: "E-waste",
    4: "Food Waste"
    }

    # Now, apply the mapping to the 'Cluster Labels' column
    test_data['Cluster Label'] = test_data['Cluster Label'].map(cluster_mapping)

    return test_data

# Example usage:
result_df = categories('test_data.csv')
