import requests
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="MemoryGPT - An LLM-powered app")

# Sidebar contents
with st.sidebar:
    st.title('MemoryGPT')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot.
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Omkar](https://portfolio-omkar.web.app/)')

# Generate empty lists for generated and past.
# generated stores AI generated responses

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["How may I help you?"]

# past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()


# User input
# Function for taking user provided prompt as input

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


# Applying the user input box
with input_container:
    user_input = get_text()


# Response output
# Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    url = 'http://127.0.0.1:6000/memory/'
    data_ojb = {
        "message": prompt,
        "type": "string",
        "userData": {
            "userName": "Mike Tyson"
        }
    }
    result = requests.post(url, json=data_ojb)
    return result.text


# Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
