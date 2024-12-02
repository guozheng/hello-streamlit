import streamlit as st
import pandas as pd

st.title('Streamlit DataFrame Demo')
st.info('There are two ways to use dataframes in Streamlit: st.dataframe and st.data_editor')

st.subheader('st.dataframe')
st.write('You can use st.dataframe to display a dataframe')
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

st.subheader('st.data_editor')
st.write('You can also use st.data_editor to edit a dataframe')

df_editable = st.data_editor(df, use_container_width=True, num_rows="dynamic", key="data_editor")
st.write('data_editor stored data in st.session_state:')
st.write(st.session_state.data_editor)
