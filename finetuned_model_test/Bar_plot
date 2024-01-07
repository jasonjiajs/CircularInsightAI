from openai import OpenAI
import pandas as pd
import numpy as np
import os
import json
import ast

data_path = "test_examples.jsonl"

# Load the dataset
with open(data_path, 'r', encoding='utf-8') as f:
    dataset = [json.loads(line) for line in f]

# Initial dataset stats
print("Num examples:", len(dataset))
print("First example:")
for message in dataset[0]["messages"]:
    print(message)

index = 0

# Get message
message = dataset[index]['messages']
system_content = message[0]['content']
user_content = message[1]['content']
assistant_content = message[2]['content']

# Set up OpenAI client
client = OpenAI(api_key="API code") # change API code to a real one 

# Get response from OpenAI API
def get_response(system_content, user_content, model):
    response = client.chat.completions.create(
        model=model,
        response_format={ "type": "json_object"},
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
            ],
        temperature=0,
        seed=0
    )
    return json.loads(response.choices[0].message.content)

def compare_outputs(index):
    # Get message
    message = dataset[index]['messages']
    system_content = message[0]['content']
    user_content = message[1]['content']
    assistant_content = message[2]['content']

    assistant_content_default = get_response(system_content, user_content, model="gpt-3.5-turbo-1106")
    assistant_content_finetuned = get_response(system_content, user_content, model="ft:gpt-3.5-turbo-1106:personal::8e9YXb9p")

    # print("--- Comparing outputs: ---")
    # print("GPT response (ground truth): ", assistant_content)
    # print("GPT response (default model): ", assistant_content_default)
    # print("GPT response (finetuned model): ", assistant_content_finetuned)

    return assistant_content, assistant_content_default, assistant_content_finetuned

assistant_contents = []
assistant_contents_default = []
assistant_contents_finetuned = []

for i in range(len(dataset)): 
    outputs = compare_outputs(i)
    
    
    # Append the relevant parts of the outputs to each list
    assistant_contents.append(outputs[0])
    assistant_contents_default.append(outputs[1])
    assistant_contents_finetuned.append(outputs[2])

data_dicts = [ast.literal_eval(item) for item in assistant_contents]

# Create a DataFrame from the list of dictionaries
assistant_contents_df = pd.DataFrame(data_dicts)

assistant_contents_default_df = pd.DataFrame(assistant_contents_default)
assistant_contents_finetuned_df = pd.DataFrame(assistant_contents_finetuned)

import pandas as pd
import matplotlib.pyplot as plt

score_counts = assistant_contents_finetuned_df.apply(pd.Series.value_counts).fillna(0)

# Reorder the index to have the scores in descending order if they are not already
score_counts = score_counts.loc[[3, 2, 1]]

# Plot a bar plot for each score count
score_counts.plot(kind='bar', subplots=True, layout=(1, 4), figsize=(14, 4), legend=False)

# Set common labels
plt.suptitle('Score Distribution for fine-tuned LLM')
plt.xlabel('Scores')
plt.ylabel('Count')

# Layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
# Show the plot
plt.show()

score_counts_default = assistant_contents_default_df.apply(pd.Series.value_counts).fillna(0)

# Plot a bar plot for each score count
score_counts_default.plot(kind='bar', subplots=True, layout=(1, 4), figsize=(14, 4), legend=False)

# Reorder the index to have the scores in descending order if they are not already
score_counts = score_counts.loc[[3, 2, 1]]

# Set common labels
plt.suptitle('Score Distribution for non-tuned LLM')
plt.xlabel('Scores')
plt.ylabel('Count')

# Layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
# Show the plot
plt.show()

score_counts_default = assistant_contents_default_df.apply(pd.Series.value_counts).fillna(0)

# Plot a bar plot for each score count
score_counts_default.plot(kind='bar', subplots=True, layout=(1, 4), figsize=(14, 4), legend=False)

# Reorder the index to have the scores in descending order if they are not already
score_counts = score_counts.loc[[3, 2, 1]]

# Set common labels
plt.suptitle('Score Distribution for non-tuned LLM')
plt.xlabel('Scores')
plt.ylabel('Count')

# Layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
# Show the plot
plt.show()


