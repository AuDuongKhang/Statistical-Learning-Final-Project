import streamlit as st
from text_input_option import function_text_input
from news_option import function_news
from upload_file_option import function_upload_file


def main():
    st.title("Text Summarization Web App")

    st.sidebar.header("Select input option")
    input_type = st.sidebar.selectbox(
        "Select option:", ("Upload file", "Text input", "News"))

    # option upload file
    if input_type == "Upload file":
        function_upload_file()

    # option text
    elif input_type == "Text input":
        function_text_input()

    # option news
    elif input_type == "News":
        function_news()


if __name__ == "__main__":
    main()
