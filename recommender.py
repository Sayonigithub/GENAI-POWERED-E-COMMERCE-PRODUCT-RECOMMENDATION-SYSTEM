import os
import pandas as pd
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

openai.api_key = os.getenv("OPENAI_API_KEY")

class ProductRecommender:
    """Uses RAG to retrieve and rank products based on natural‑language queries."""

    def __init__(self, df):
        self.df = df
        self.texts = df['description'].fillna('').tolist()
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = FAISS.from_texts(self.texts, self.embeddings)

    def recommend(self, query: str, k: int = 5) -> pd.DataFrame:
        """Return top‑k recommended products."""
        docs = self.vector_store.similarity_search(query, k=k)
        idx = [self.texts.index(doc.page_content) for doc in docs]
        return self.df.iloc[idx].reset_index(drop=True)
