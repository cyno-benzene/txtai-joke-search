import streamlit as st
import pandas as pd
from txtai import Application

# reder the python notebooks for saving embeddings 
embeddings_path = "./data/jokes.tar.gz" 

app = Application(f"path: {embeddings_path}")

results_limit_options = [10, 20, 50, 100]

def context(query, limit):
    return app.search("select text, answer, score from txtai where similar(:query)", parameters={"query": query}, limit=limit)

st.set_page_config(page_title="Jokes search using txtai", page_icon="🤡", layout="wide")

st.title("Jokes search using txtai")

results_limit = st.slider("Select number of results to display:", min_value=10, max_value=100, value=10, step=10)

query = st.text_input("Enter your search query:")


if query:
    result = context(query, results_limit)

    st.write(f"Search results for: {query}")

    num_columns = 3 

    cols = st.columns(num_columns)

    for index, joke in enumerate(result):
        
        with cols[index % num_columns]:  
            
            container = st.container(border=True)

            container.markdown(f"<h3 style='color:white;'>{joke['text']}</h3>", unsafe_allow_html=True)
            
            container.markdown(f"<p style='color:white;'>{joke['answer']}</p>", unsafe_allow_html=True)

            container.markdown(f"<p style='color:grey;'><strong>Score:</strong> {joke['score']}</p>", unsafe_allow_html=True)





