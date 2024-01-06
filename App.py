######################## App.py ################################
import streamlit as st
import pandas as pd
import openai
import json 
import re 
import helper
from datetime import datetime
import Templates
import similar_emails

openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = "https://###"  # Your Azure OpenAI resource's endpoint value.
openai.api_key = "####" # YOUR API KEY

feedback_file = 'feedback.csv'

st.set_page_config(page_title="Email Assistant Tool", layout="wide")
st.title('Email Assistant Tool')

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div style="border: 1px solid #d3d3d3; border-radius: 5px; padding: 10px;">
    
    **How to define a category?**

    Write your email in the text area. Feel free to adapt the category if it is misclassified by our model.
    
    ''', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div style="border: 1px solid #d3d3d3; border-radius: 5px; padding: 10px;">
    
    **Generate reply**
    
    Once the category is defined, you can generate the reply by clicking the button below.
    ''', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

#openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
st.session_state['agent_name'] = st.sidebar.text_input('Agent Name')

################ Define Session State ###################
#session_state = st.session_state
if 'auto_repliable_category' not in st.session_state:
    st.session_state['auto_repliable_category'] = None

if 'pri_category' not in st.session_state:
    st.session_state['pri_category'] = None

if 'sec_category' not in st.session_state:
    st.session_state['sec_category'] = None

if 'cat_instruction' not in st.session_state:
    st.session_state['cat_instruction'] = None

if 'similar_emails' not in st.session_state:
    st.session_state['similar_emails'] = None

if 'similar_emails_replies' not in st.session_state:
    st.session_state['similar_emails_replies'] = None

if 'agent_name' not in st.session_state:
    st.session_state['agent_name'] = None

# Function to handle feedback submission
def handle_feedback(model_pred, email_text, agent_update, user_comment=None):
    with open(feedback_file, mode='a') as f:
        pd.DataFrame({
            'timestamp': [datetime.now()],
            'email': [email_text],
            'model_pred': [model_pred],
            'agent_update': [agent_update],
            'user_comment': [user_comment],
        }).to_csv(f, index=False, header=f.tell()==0)
    st.session_state['auto_repliable_category'] = agent_update["category"]
    st.session_state['pri_category'] = agent_update["primary_task"]
    st.session_state['sec_category'] = agent_update["secondary_task"]
    st.success('Category updated and feedback recorded.')
    return


st.markdown('## Enter a Client Email to Process')
text = st.text_area('', '')

## Function to allow agent to change the categories predicted by the llm
def allow_change_repliable_cat():
    change_cat = st.checkbox('Can be Automated')
    if change_cat:
        st.session_state['auto_repliable_category'] = 0


## Function to handle subsequence actions after the agent submit the email
## Will run llm to predict the category and task category
def on_submit():
    # print(helper.clean_json_string(helper.get_response(Templates.get_task_and_instruction, text)))
    # No matter the llm_repliable category, we need to get the simialr emails
    out = similar_emails.get_most_similar_emails(text)
    st.session_state['similar_emails'] = out[1]
    st.session_state['similar_emails_replies'] = out[2]

    # Get the email repliable category
    response = helper.get_response(Templates.identify_automated_category_system_prompt_template, text)
    llm_category = eval(response)
    
    if llm_category == 0:
        st.session_state['auto_repliable_category'] = 0
        pass
    elif llm_category == 1:
        st.write("This email is too complex")
        st.session_state['auto_repliable_category'] = 1
    elif llm_category == 2:
        st.session_state['auto_repliable_category'] = 2
        st.write("This email does not need a reply")
        
submit_button = st.button('Submit')

if submit_button:
    on_submit()
#option1 = st.selectbox('Email Category', ('confirm_booking_cancellation', 'booking_status_inquiry', 'roll_a_booking'), index=0)

# if the email is repliable, then pass the email to anther llm to get the task category
if st.session_state['auto_repliable_category'] == 0:
    llm_task_instruction = json.loads(helper.clean_json_string(helper.get_response(Templates.get_task_and_instruction, text)))
    pri_cat = llm_task_instruction.get('Primary', None)
    sec_cat = llm_task_instruction.get('Secondary', None)
    cat_instra = llm_task_instruction.get('Instruction', None)
    st.session_state['pri_category'] = pri_cat
    st.session_state['sec_category'] = sec_cat
    st.session_state['cat_instruction'] = cat_instra
    st.write("Primary Task Category: ", st.session_state['pri_category'], " ----- Secondary Task Category: ", st.session_state['sec_category'])

# Button to allow users to change the category
# choose another option if selected_category is not correct. Default option is the current selected_category
change_category = st.checkbox('Change the Category')
if change_category:
    st.write('0: The reply can be automated', '1: The email is too complex', 
                    '2: The email does not require a reply')
    option_auto = st.selectbox('Automatable', (Templates.automatable_cats), index=0)
    if option_auto == 0:
        # st.session_state['auto_repliable_category'] = 0
        option1 = st.selectbox('Primary Task Category', (Templates.primary_cats), index=1)
        if option1 == "billing_support":
            option2 = st.selectbox('Secondary Task Category', (Templates.billing_sec_cats), index=1)
        elif option1 == "booking_support":
            option2 = st.selectbox('Secondary Task Category', (Templates.booking_support_sec_cats), index=1)
        elif option1 == "seaway_bills_support":
            option2 = st.selectbox('Secondary Task Category', (Templates.seaway_bills_secondary_cats), index=1)

        user_comment = st.text_area("Enter your comment here", "")
        if st.button('Update'):
            model_output = {"category":st.session_state['auto_repliable_category'],
                            "primary_task":st.session_state['pri_category'],
                            "secondary_task":st.session_state['sec_category']}
            agent_update = {"category":option_auto,
                            "primary_task":option1,
                            "secondary_task":option2}
            handle_feedback(model_output, text, agent_update, user_comment)
    elif option_auto == 1:
        # st.session_state['auto_repliable_category'] = 1
        user_comment = st.text_area("Enter your comment here", "")
        if st.button('Update'):
            model_output = {"category":st.session_state['auto_repliable_category'],
                            "primary_task":st.session_state['pri_category'],
                            "secondary_task":st.session_state['sec_category']}
            agent_update = {"category":option_auto,
                            "primary_task":None,
                            "secondary_task":None}
            handle_feedback(model_output, text, agent_update, user_comment)

    elif option_auto == 2:
        # st.session_state['auto_repliable_category'] = 2
        user_comment = st.text_area("Enter your comment here", "")
        if st.button('Update'):
            model_output = {"category":st.session_state['auto_repliable_category'],
                            "primary_task":st.session_state['pri_category'],
                            "secondary_task":st.session_state['sec_category']}
            agent_update = {"category":option_auto,
                            "primary_task":None,
                            "secondary_task":None}
            handle_feedback(model_output, text, agent_update, user_comment)


########## END of Classification Part #########
st.divider()
########## BEGIN of Reply Part #########

## Only use this part when the email is identified as repliable
if st.session_state['auto_repliable_category'] == 0:
    status_box = 'None'
    status_selection = ['Confirmed', 'Not Confirmed']
    if st.session_state['sec_category'] == 'confirm_booking_cancellation':
        status_box = 'Booking Cancelled?'
    elif st.session_state['sec_category'] == 'booking_status_inquiry':
        status_box = 'Booking Status?'
        status_selection = ['On Hold', 'Delayed', 'Rail Team', 'Door Team', 'Damaged']
    elif st.session_state['sec_category'] == 'roll_a_booking':
        status_box = 'Booking Rolled?'
    elif st.session_state['sec_category'] == 'update_seaway_bill':
        status_box = 'Seaway Bill Updated?'

    option = st.selectbox(status_box, (status_selection))

    # Handle logic for confirmed or not confirmed bookings
    if option == 'Confirmed':
        # Handle confirmed booking logic
        reply_info = "request status: "+option+" meaning use the confirmed template. agent name: "+st.session_state['agent_name'] 
        pass
    else:
        reason = st.text_area("Enter Reason Here", "Optional")
        action = st.text_area("Enter Action Here", "Optional")
        reply_info = "request status: "+option+". agent name: "+st.session_state['agent_name'] + ". reason: " + reason + ". action: " + action


    if st.button('Generate'):
        # Generate email reply logic
        if st.session_state['sec_category'] == 'booking_status_inquiry':
            email_reply = helper.get_response(Templates.delivery_status_reply, reply_info)
        elif st.session_state['sec_category'] == 'confirm_booking_cancellation':
            email_reply = helper.get_response(Templates.confirm_booking_cancellation_reply, reply_info)
        elif st.session_state['sec_category'] == 'roll_a_booking':
            email_reply = helper.get_response(Templates.roll_a_booking_reply, reply_info)
        elif st.session_state['sec_category'] == 'update_seaway_bill':
            email_reply = helper.get_response(Templates.update_bill_reply, reply_info)
        st.markdown('## Email Reply')
        # write the email reply and allow the user to copy it to clipboard
        st.code(email_reply, language='html')

########## END of Reply Part #########
st.divider()
########## BEGIN of Similar Email Part #########

with st.expander("See Similar Emails"):
    df = pd.DataFrame(columns=['Email', 'Reply'])
    #st.write(st.session_state['similar_emails'])
    #st.write(st.session_state['similar_emails_replies'])
    if st.session_state['similar_emails'] != None:
        for i in range(len(st.session_state['similar_emails'])):
            email = st.session_state['similar_emails'][i]
            reply = st.session_state['similar_emails_replies'][i]
            new_pair = pd.DataFrame({'Email':[email], 'Reply':[reply]})
            df = pd.concat([df, new_pair], ignore_index=True)
        st.dataframe(df, use_container_width=True)


########### For DEMO Purpose ONLY, allow user to see feedback csv ###########
with st.expander("View feedback dataframe"):
    try:
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Feedback CSV file not found.")
    # df = pd.read_csv("feedback.csv")
    # st.dataframe(df)