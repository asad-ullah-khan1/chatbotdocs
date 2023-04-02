import streamlit as st
from main import ask_bot


st.title('Ask docs ')

user_query = st.text_area('What do you want to ask ?')

if user_query is not None:
    response = ask_bot('index.json',user_query)
    st.write(response)
