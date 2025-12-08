import streamlit as st
import requests

BASE_URL = "https://text-utility-161s.onrender.com"

st.title("Text Utility App")
st.write("Summary, Sentiment, Wordcount, Keywords — all in one UI")

text_input = st.text_area("Enter your text:")

option = st.selectbox(
    "Choose action:",
    ("Summary", "Sentiment", "Wordcount", "Keywords")
)

if st.button("Run"):
    if not text_input.strip():
        st.warning("Please enter some text!")
    else:
        if option == "Summary":
            resp = requests.post(f"{BASE_URL}/summary", json={"text": text_input})
            st.json(resp.json())

        elif option == "Sentiment":
            resp = requests.post(f"{BASE_URL}/sentiment", json={"text": text_input})
            st.json(resp.json())

        elif option == "Wordcount":
            resp = requests.post(f"{BASE_URL}/wordcount", json={"text": text_input})
            st.json(resp.json())

        elif option == "Keywords":
            resp = requests.post(f"{BASE_URL}/keywords", json={"text": text_input})
            st.json(resp.json())
