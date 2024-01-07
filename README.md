An overview of what each folder and file do:
/Data
- consist of original data, splitted data, and code to split data. It also have the manually labeled data set which was used as ground truth
- /Json: consist of json version of the csv file

/Preprocessing
- Code to convert csv file into json file, the json data file are saved in /Data

/finetuned_model_test
- consist of llm fine tune test file, code that generated the plot and accuracy rate

/web_interface
- **Everthing you need to run Streamlit**

/clusters
- code of k-mean method to get the categories of the ideas

/api_key_test
- code to test the gpt api key
