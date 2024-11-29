import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Layout Demo')

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input("Enter your name:")

with col2:
    if user_input:
        st.header(f"Hello, {user_input}!")

with st.container(border=True):
    if st.button("Click me!"):
        st.write("Surprise!")
        st.image("https://cdn2.steamgriddb.com/icon/a1d6bb888d7e07c46fe551c03b10bdc2/32/96x96.png")

with st.expander("Click to open chart"):
    df = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.line_chart(df)
