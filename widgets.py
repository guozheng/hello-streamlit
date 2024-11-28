import streamlit as st
import pandas as pd
import time

st.title('Widgets')

left, right = st.columns(2)

with left:
    st.text_input('Enter your name', key='name')
    st.write(f'{st.session_state.name}')

    if st.button('Show/Hide current time'):
        st.write('Current time:', pd.Timestamp.now().strftime('%I:%M:%S %p'))

with right:
    selection = st.selectbox('Select a value for seconds to complete', [1, 2, 3, 4])
    # st.write(f'Wait for: {selection} seconds to complete')

    if st.button('Start Progress'):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(selection/100)
            progress_bar.progress(i + 1)
        st.success('Completed!')