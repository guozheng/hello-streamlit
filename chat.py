import streamlit as st
import requests
import time

def fetch_message():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else:
        return "Can you say it again?"

st.title("Chat Demo")
user_input = st.chat_input("Enter a message:")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        message = fetch_message()
        with st.spinner("Thinking..."):
            time.sleep(2)
        st.write(message)