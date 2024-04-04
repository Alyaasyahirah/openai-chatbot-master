
import openai
import streamlit as st


st.write('Hello, *World!* :sunglasses:')

with st.sidebar:
  st.title(' OpenAI Chatbot')
  if 'OPENAI_API_KEY' in st.secrets:
    st.success('API key already provided!', icon='✅')
    openai.api_key = st.secrets['OPENAI_API_KEY']
  else:
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-') and len(openai.api_key) == 51):
      st.warning('Please enter your credentials!', icon='⚠️')
    else:
      st.success('Proceed to entering your prompt message!', icon='')

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  with st.chat_message("assistant"):
    full_response = ""
    for response in openai.chat.completions.create(
       ):
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        stream=True
  #  ):
    st.markdown(response.choices[0].message.content)
