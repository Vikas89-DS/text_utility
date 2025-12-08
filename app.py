# ui.py  ← final working version

import streamlit as st
import requests

API_URL = "https://text-utility-161s.onrender.com"

st.set_page_config(page_title="Text Utility Tool", layout="centered")

st.title("Text Utility Tool")
st.markdown("**Extract keywords • Count words • Detect sentiment • Generate summary**")

text = st.text_area("Enter your text here", height=200, placeholder="Paste or type any text...")

if st.button("Analyze Text", type="primary", use_container_width=True):
    if text.strip():
        with st.spinner("Processing..."):
            try:
                kw   = requests.post(f"{API_URL}/keywords",   json={"text": text}).json()
                wc   = requests.post(f"{API_URL}/wordcount",  json={"text": text}).json()
                sent = requests.post(f"{API_URL}/sentiment",  json={"text": text}).json()
                summ = requests.post(f"{API_URL}/summary",    json={"text": text}).json()

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Keywords")
                    keywords = kw.get("keywords", [])
                    if keywords:
                        st.write(", ".join(sorted(keywords)))
                    else:
                        st.info("No keywords found")

                    st.subheader("Word Count")
                    st.metric("Total Words", wc.get("wordcount", 0))

                with col2:
                    st.subheader("Sentiment")
                    sentiment = sent.get("sentiment", "neutral").capitalize()
                    if sentiment == "Positive":
                        st.success(sentiment)
                    elif sentiment == "Negative":
                        st.error(sentiment)
                    else:
                        st.info(sentiment)

                    st.subheader("Summary")
                    st.write(summ.get("summary", "No summary generated"))

            except Exception as e:
                st.error("API not responding. Try again in 2-3 seconds (Render free plan sleeps).")
    else:
        st.warning("Please enter some text first")

st.caption("Powered by FastAPI + Streamlit • Hosted on Render")