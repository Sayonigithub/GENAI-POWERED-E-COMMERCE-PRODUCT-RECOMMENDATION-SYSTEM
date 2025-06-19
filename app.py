import streamlit as st
import pandas as pd
from pathlib import Path
from backend.recommender import ProductRecommender

st.set_page_config(page_title="GENAI Product Recommender", page_icon="🛍️")
st.title("🛍️ GENAI Product Recommendation System")
st.caption("Powered by RAG + NLP • OpenAI • Langchain")

@st.cache_resource
def load_data():
    return pd.read_csv(Path(__file__).parent.parent / "data" / "products.csv")

data = load_data()
recommender = ProductRecommender(data)

query = st.text_input("Describe what you need (brand, budget, category…):")

if query:
    results = recommender.recommend(query)
    st.subheader("🎯 Top Picks")
    st.dataframe(results)
