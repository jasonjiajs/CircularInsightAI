import openai
import json 
import re 

def get_response(system_prompt, user_prompt):
    response = openai.ChatCompletion.create(
        engine="CMA-CGM-gpt-35-turbo-SBX-NAM",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    output = response['choices'][0]['message']['content']
    return output

def clean_json_string(json_string):
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_string)