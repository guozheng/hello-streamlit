import streamlit as st

st.title("Secret Manager Demo")
st.info("Store your secrets in .streamlit/secrets.toml")

env = st.selectbox('Select environment:', ['', 'dev', 'prod'])

if env:
    st.write(f"Selected environment: {env}")
    st.write(f"Secret: {st.secrets[env]['openai']}")