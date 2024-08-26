from summarize_text import summarize_text
import streamlit as st


# encoding the file
def read_file_with_encoding_detection(uploaded_file):
    encodings = ['utf-8', 'utf-16', 'latin-1']
    for encoding in encodings:
        try:
            return uploaded_file.read().decode(encoding)
        except UnicodeDecodeError:
            continue
    st.error("Error can not read this file")
    return None


# UI for upload file
def function_upload_file():
    file_text = None
    uploaded_file = st.file_uploader(
        "Upload text file", type=["txt", "pdf", "docx"])

    if uploaded_file is not None:
        try:
            file_text = read_file_with_encoding_detection(uploaded_file)
            st.write("Text from upload file:")
            st.write(file_text)
        except UnicodeDecodeError:
            st.error("Error can not read the text file")

    if file_text:
        if st.button("Summarize"):
            summarized_text = summarize_text(file_text)
            st.write("Summarize text:")
            st.write(summarized_text)
