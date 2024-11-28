import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.title('My First Streamlit App')

# Add a header
st.header('Welcome to the Demo!')

# Add some text
st.write('This is a simple demonstration of Streamlit features.')

# Create a sidebar
st.sidebar.header('Sidebar Controls')

# Add a slider to the sidebar
number = st.sidebar.slider('Select a number:', 0, 100, 50)
st.write(f'You selected: {number}')

# Create a sample dataframe
data = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})

# Display the dataframe
st.subheader('Sample DataFrame')
st.dataframe(data)

# Create a line chart
st.subheader('Line Chart')
st.line_chart(data)

# Add a button
if st.button('Click me!'):
    st.balloons()
    st.write('🎉 Thanks for clicking!')

# Add a selectbox
option = st.selectbox(
    'What is your favorite color?',
    ['Red', 'Blue', 'Green', 'Yellow']
)
st.write(f'Your favorite color is {option}') 