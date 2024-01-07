import streamlit as st
from openai import OpenAI
import pandas as pd
import numpy as np
import os
import json
import preprocessing
import altair as alt
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/jasonjiajs/ai-earthhack)"

# Set up OpenAI client
try:
    openai_api_key=os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except:
    if openai_api_key is not None:
        client = OpenAI(api_key=openai_api_key)

st.title("📝 Circular Economy Idea Evaluator")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

uploaded_file = st.file_uploader("Upload the csv file", type=("csv"))

# question = st.text_input(
#     "Ask something about the article",
#     placeholder="Can you give me a short summary?",
#     disabled=not uploaded_file,
# )

if uploaded_file and not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")

# How can this tool help you?
st.write("### How can this tool help you?")

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

@st.cache_data(show_spinner=False)
def get_df_metrics(uploaded_file):
    df_full, df, contains_labels = preprocessing.read_data(uploaded_file)
    df_full['category'] = np.random.choice(['Plastics', 'Fashion', 'Food', 'Others'], size=len(df_full))
    df = df.iloc[:2, :] # reduce the number of rows during development
    df_metrics = preprocessing.get_metrics_for_filtering_ideas(df_full, df, client, finetuned=True)
    return df_full, df, df_metrics

if uploaded_file and openai_api_key:
    df_full, df, df_metrics = get_df_metrics(uploaded_file)
    
    st.write("### Data")
    # Top menu
    top_menu = st.columns(3)
    with top_menu[0]:
        category_filter = st.multiselect("Filter by Category", options=df_metrics['category'].unique(), default=df_metrics['category'].unique())
    with top_menu[1]:
        sort_field = st.selectbox("Sort By", options=df_metrics.columns, index=df_metrics.columns.get_loc('overall_score'))
    with top_menu[2]:
        sort_direction = st.radio("Direction", options=["⬆️", "⬇️"], horizontal=True, index=1)
    df_metrics_interface = df_metrics[df_metrics['category'].isin(category_filter)]
    df_metrics_interface = df_metrics_interface.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)

    # Table
    pagination = st.container()

    # Bottom Menu
    bottom_menu = st.columns((4, 1, 1))
    with bottom_menu[2]:
        batch_size = st.selectbox("Page Size", options=[25, 50, 100])
    with bottom_menu[1]:
        total_pages = (
            int(len(df_metrics_interface) / batch_size) if int(len(df_metrics_interface) / batch_size) > 0 else 1
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")

    pages = split_frame(df_metrics_interface, batch_size)
    if df_metrics_interface.shape[0] > 0:
        pagination.dataframe(data=pages[current_page - 1], use_container_width=True)
        # Show distribution of overall_score
        st.write("### Distribution of overall_score")    
        bar_chart = alt.Chart(df_metrics_interface).mark_bar().encode(
                x="sum(overall_score):Q",
                y="overall_score:O",
                color="category:N"
            )
        st.altair_chart(bar_chart, use_container_width=True)
    else:
        pagination.error("Select at least one category")
