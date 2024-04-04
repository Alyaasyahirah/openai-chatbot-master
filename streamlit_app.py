
import openai
import streamlit as st



st.header('Im Creative Idea', divider='rainbow')
st.write('Hello, *World!* :rose::hibiscus::sunflower::blossom:')
st.write("you can choose age for appropriate creative content")
st.divider()

st.slider("range your age", 0, 100, (15, 75))

st.divider()  # 👈 Draws a horizontal rule
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


    if prompt := st.chat_input("Say something"):  #start input chat
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}") #end
    full_response = ""
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=False
        )
    st.markdown(response.choices[0].message.content)
