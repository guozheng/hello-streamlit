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

# initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

# show messages in the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# now take user input and store it in the history
if user_input := st.chat_input("Enter a message:"):
    with st.chat_message("user"):
        st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("assistant"):
        message = fetch_message()
        with st.spinner("Thinking..."):
            time.sleep(2)
        st.write(message)
        st.session_state.messages.append({"role": "assistant", "content": message})