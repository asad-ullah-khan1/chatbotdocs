import streamlit as st

st.set_page_config(
    page_title="Q/A bot for Text files",
    page_icon="👋",
)

st.write("# Welcome to inteliText Q/A chatbot! 👋")

st.sidebar.success("Select a Page from above menu")

st.markdown(
    """
    ## Now you can Talk to your Text Files/Data

Looking for a versatile chatbot that can handle various tasks and improve your workflow? Look no further than our AI-powered chatbot! Our chatbot is designed to help you with a variety of tasks, from answering customer inquiries to automating routine business operations.


## Benefits of Our Chatbot

- Saves you time and resources by automating customer interactions
- Provides instant responses to customer inquiries, improving customer satisfaction
- Offers personalized recommendations based on user data and behavior
- Enables you to focus on more strategic business initiatives

## How Our Chatbot Works

Our chatbot uses natural language processing and machine learning algorithms to understand user queries and provide accurate responses. Simply upload your text files to the chatbot, and it will retrieve relevant information based on user requests.

## How to Use Our Chatbot

1. Go to the upload page by clicking on "/upload".
2. Once on the upload page, select the text file you want to upload.
3. Click on the "Upload" button to upload the file.
4. After uploading the file, go to the chatbot page by clicking on "/chatbot".
5. Type in your question with the context of the uploaded file.
6. The chatbot will provide relevant information based on your query.

## Try Our Chatbot Today

Don't miss out on the opportunity to improve your customer experience and streamline your operations. Try our chatbot today and see the results for yourself!

"""
)
