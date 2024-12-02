import streamlit as st

st.title("Session State Demo")

if "counter" not in st.session_state:
    st.session_state.counter = 0

# This counter is not part of the session state, so it will be reset to 0 at each run
counter2 = 0

if st.button("Increment"):
    st.session_state.counter += 1
    counter2 += 1

st.info(f"Counter in session state: {st.session_state.counter}, Counter outside session state: {counter2}")

st.divider()

# bind widget state in session state
if "temperature" not in st.session_state:
    st.session_state.temperature = 0

st.slider("Temperature in Fahrenheit:", min_value=0, max_value=100, key="temperature")

st.info(f"Temperature in session state: {st.session_state.temperature}")