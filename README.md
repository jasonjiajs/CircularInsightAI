# CircularInsightAI
Hackathon Project - AI EarthHack <br>
Team Members: [Jason Jia](https://www.linkedin.com/in/jasonjiajs/), [Maria Besedovskaya](https://www.linkedin.com/in/mariabesedovskaya/), [Nuobei Zhang](https://www.linkedin.com/in/nuobeizhang/), [Xidan Xu](https://www.linkedin.com/in/xidan-xu/)

<img src="readme_banner.jpeg" alt="banner" height="350">

## Summary
We built [CircularInsightAI](https://circularinsightai-ai-earthhack.streamlit.app/), an AI-powered system that innovatively evaluates circular economy ideas using a multi-faceted filter and enhancer approach. It is designed to empower investors in making efficient and informed assessments.

## Final Report
[Link to Final Report](https://docs.google.com/document/d/1gNMZ4yrDLwVwqaGnleMvuPU7mQ7gQR77j5N13ePDV28/edit?usp=sharing)

## Repo Directory

An overview of what each folder and file does:

`/data`

- Consists of original data, splited data, and code to split data. It also has the manually labeled data set which was used as ground truth
- `data/json`: consists of JSON version of the CSV file

`/preprocessing`

- Code to convert CSV file into JSON files, which are saved in `data/json`

`/finetuned_model_test`

- Consists of LLM fine-tuning test files and code that generated the plots and accuracy rates

`/web_interface`

- Self-contained folder containing all files needed to run the Streamlit web interface
- To run the web interface locally, `cd` to the root of this repo and run `streamlit run web_interface/CircularInsightAI.py`.

`/clusters`

- Code of k-means method to get categories of ideas

`/api_key_test`

- Code to test the GPT API key
