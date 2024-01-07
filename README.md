# CircularInsightAI
Hackathon Project - AI EarthHack <br>
Team Members: [Jason Jia](https://www.linkedin.com/in/jasonjiajs/), [Maria Besedovskaya](https://www.linkedin.com/in/mariabesedovskaya/), [Nuobei Zhang](https://www.linkedin.com/in/nuobeizhang/), [Xidan Xu](https://www.linkedin.com/in/xidan-xu/)

<img src="readme_banner.jpeg" alt="banner" height="350">

## Overview

An overview of what each folder and file does:

`/data`

- Consists of original data, splited data, and code to split data. It also has the manually labeled data set which was used as ground truth
- `data/json`: consists of JSON version of the CSV file

`/preprocessing`

- Code to convert CSV file into JSON files, which are saved in `data/json`

`/finetuned_model_test`

- Consists of LLM fine-tuning test files and code that generated the plots and accuracy rates

`/web_interface`

- Self-contained folder containing all code and resources needed to run the Streamlit web interface

`/clusters`

- Code of k-means method to get categories of ideas

`/api_key_test`

- Code to test the GPT API key
