import streamlit as st
from main import construct_index
import os
from pathlib import Path

st.title('Upload a file')



uploaded_file = st.file_uploader(label="upload text file/files", accept_multiple_files=True)

def save_file_to_folder(uploadedFile):
    # Save uploaded file to 'content' folder.
    save_folder = 'content'
    save_path = Path(save_folder, uploadedFile.name)
    with open(save_path, mode='wb') as w:
        w.write(uploadedFile.getvalue())

    if save_path.exists():
        st.success(f'File {uploadedFile.name} is successfully saved!')


if uploaded_file:
    for file in uploaded_file:
        save_file_to_folder(file)


index = construct_index('content')