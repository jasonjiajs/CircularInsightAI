An overview of what each folder and file do:

/Data
- consist of original data, splited data, and code to split data. It also has the manually labeled data set which was used as ground truth
- /Json: consists of JSON version of the CSV file

/Preprocessing
- Code to convert CSV file into JSON file, the JSON data file are saved in /Data

/finetuned_model_test
- consist of LLM fine-tune test file, code that generated the plot and accuracy rate

/web_interface
- **Everything you need to run Streamlit**

/clusters
- code of the k-mean method to get the categories of the ideas

/api_key_test
- code to test the GPT API key
