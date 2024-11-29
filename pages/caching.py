import streamlit as st
import time
import pandas as pd
import numpy as np

# Using st.cache_data for data that doesn't change often
@st.cache_data
def load_data():
    # Simulate loading large dataset
    time.sleep(2)  # Simulate delay
    df = pd.DataFrame(
        np.random.randn(1000, 5),
        columns=['A', 'B', 'C', 'D', 'E']
    )
    return df

# Using st.cache_resource for objects that need to be shared across sessions
@st.cache_resource
def create_expensive_computation():
    # Simulate expensive computation
    time.sleep(3)
    return np.random.randn(100)

st.title('Streamlit Caching Demo')

# Demo cache_data
st.header('Demo: st.cache_data')
st.write('This data loading is cached. Click the button multiple times - first load will be slow, subsequent loads will be instant')

if st.button('Load Data'):
    data = load_data()
    st.dataframe(data.head())
    st.success('Data loaded!')

# Demo cache_resource 
st.header('Demo: st.cache_resource')
st.write('This computation is cached and shared across sessions')

if st.button('Run Expensive Computation'):
    result = create_expensive_computation()
    st.line_chart(result)
    st.success('Computation complete!')

st.info('Note: The @st.cache_data decorator is used for data that changes occasionally, while @st.cache_resource is used for objects that should persist across multiple sessions.')
