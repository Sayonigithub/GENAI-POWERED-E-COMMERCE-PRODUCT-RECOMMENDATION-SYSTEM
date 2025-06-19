# 🛍️ GENAI‑Powered E‑Commerce Product Recommendation System

This project demonstrates a RAG‑enhanced recommendation engine that serves personalised product suggestions based on conversational queries.

## 🎯 Highlights
* Natural‑language understanding with OpenAI embeddings
* Vector search via FAISS for fast retrieval
* Streamlit UI for instant previews
* Modular design: swap data or models effortlessly

## 🚀 Quick Start
```bash
./setup.sh
```

## 📂 Structure
```
├── backend/
│   ├── __init__.py
│   └── recommender.py
├── frontend/
│   └── app.py
├── data/
│   └── products.csv
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .streamlit/
│   └── config.toml
├── setup.sh
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🔑 Environment
```bash
export OPENAI_API_KEY="sk-..."
```

## 🐣 Sample Queries
* "Affordable smartphones under 20k"
* "Laptop with SSD and 16GB RAM"
* "Running shoes for women"

## 🤝 Contributing
PRs welcome!

## 📄 License
MIT
