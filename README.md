
---

# Text_2_SQL: RAG-based Natural Language to SQL

A robust **Retrieval-Augmented Generation (RAG)** system designed to bridge the gap between natural language and relational databases. This project allows users to query SQL databases using plain English, leveraging **LangChain** for orchestration, **Qdrant** for schema context retrieval, and **Ollama** for private, local LLM inference.

## 🚀 Features

* **Local-First:** Runs entirely on your machine using Ollama—no API keys required for inference.
* **RAG-Enhanced:** Uses a vector database (Qdrant) to store database metadata, ensuring the LLM understands your specific schema before generating queries.
* **Natural Language Interface:** Translate complex business questions into accurate SQL joins and aggregations.
* **Secure:** Since it runs locally, your sensitive database schema and data never leave your infrastructure.

---

## 🛠️ Tech Stack

* **Framework:** [LangChain](https://www.langchain.com/)
* **Vector Database:** [Qdrant](https://qdrant.tech/)
* **LLM Engine:** [Ollama](https://ollama.ai/) (e.g., Llama 3, Mistral, or SQLCoder)
* **Database Support:** SQLite, PostgreSQL, or MySQL (via SQLAlchemy)
* **Language:** Python 3.10+

---

## 📋 Prerequisites

1. **Ollama:** [Download and install](https://ollama.ai/) Ollama.
2. **Model:** Pull a coding or general-purpose model:
```bash
ollama pull llama3

```


3. **Qdrant:** Run Qdrant locally via Docker:
```bash
docker run -p 6333:6333 qdrant/qdrant

```



---

## ⚙️ Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/Pratham1603/Text_2_SQL.git
cd Text_2_SQL

```


2. **Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configuration:**
Create a `.env` file in the root directory and add your database credentials:
```env
DB_URL=sqlite:///./example.db
QDRANT_HOST=localhost
QDRANT_PORT=6333
OLLAMA_MODEL=llama3

```



---

## 📖 How It Works

1. **Schema Indexing:** The system parses your SQL schema (tables, columns, types) and generates descriptive embeddings. These are stored in **Qdrant**.
2. **Contextual Retrieval:** When a user asks a question, the system retrieves the most relevant table schemas from the vector store.
3. **Prompt Engineering:** LangChain constructs a prompt containing the user's question and the retrieved schema context.
4. **SQL Generation:** The **Ollama** LLM generates a syntactically correct SQL query.
5. **Execution:** The system executes the query against the database and returns the result in human-readable format.

---

## 🖥️ Usage

Run the main application:

```bash
python main.py

```

**Example Query:**

> "Show me the top 5 customers who spent the most money in 2023."

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
