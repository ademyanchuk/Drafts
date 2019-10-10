import streamlit as st

def run_sentiment_analysis(txt: str) -> str:
    return ("I don't no yet!", 0.9), ("This is good!", 0,1)

algo = st.sidebar.selectbox('Algorithm:', ['Embeedings', 'JaroWinkler'])

k = st.sidebar.slider('Number of closest sentences to show', 1, 10, 5)

txt = st.text_input('Job title here:', 'Software eng')

if algo.lower() == 'jarowinkler':
    res = "I'm Roman's piece of shit"
else:
    res = run_sentiment_analysis(txt)

st.write('Closest job titles:', res)