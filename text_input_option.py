from summarize_text import summarize_text
import streamlit as st


# UI for input text option
def function_text_input():
    user_input = st.text_area("Input text to summarize", height=250)

    if st.button("Summarize"):
        summarized_text = summarize_text(user_input)
        st.write("Summarize text:")
        st.write(summarized_text)
