from langchain import OpenAI
import os
from gpt_index import SimpleDirectoryReader, ServiceContext , GPTListIndex, GPTSimpleVectorIndex,  PromptHelper,LLMPredictor
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 256
    max_chunk_overlap=20
    chunk_size_limit=600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit)

    # define LLM 
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')

    return index

def ask_bot(input_index = 'index.json', user_query="What do you want to ask ?"):
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    while True:
        query = user_query
        response = index.query(query, response_mode="compact")
        return response.response



index = construct_index('content')

