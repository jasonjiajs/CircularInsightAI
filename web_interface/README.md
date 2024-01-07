# 🎈CircularInsightAI App

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)

## Overview of the App

This app showcases an AI tool built with GPT and ML techniques that aims to help evaluators filter and score ideas.

Current examples include:

- Idea Filter
  - Allow evaluators to set a cut-off score to filter out ideas that are not relevant or too vague.

- Idea Enhancer
  - Assist evaluators to dive deep into the promising ideas and find the most innovative, feasible, and scalable idea.
  - Assist evaluators to expand on the promising ideas to be able to implement the ideas in real life.

## Demo App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://circularinsightai-ai-earthhack.streamlit.app/)

### Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps, do the following:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API key into the text box as follows:

```sh
OPENAI_API_KEY='xxxxxxxxxx'
```

## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run CircularInsightAI.py
```

To exit:
```sh
deactivate
```
