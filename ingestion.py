import sqlite3
from langchain_ollama import OllamaEmbeddings
#from langchain_community.vectorstores import Qdrant
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http import models

def setup_db():
    # Create local SQLite database
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT, city TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INT, user_id INT, amount REAL)")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'Pratham', 'Mumbai'), (2, 'Gemini', 'Google')")
    cursor.execute("INSERT OR IGNORE INTO orders VALUES (101, 1, 500.0), (102, 2, 1200.0)")
    conn.commit()
    conn.close()

def index_schema():
    setup_db()
    # Descriptions that help the AI understand your tables
    texts = [
        "Table 'users' has columns: id, name, city. Use for identity and location info.",
        "Table 'orders' has columns: id, user_id, amount. Use for sales and transaction info."
    ]
    
    embeddings = OllamaEmbeddings(model="llama3:latest")
    client = QdrantClient("http://localhost:6333")
    
    # Reset collection for a clean start
    client.recreate_collection(
        collection_name="db_schema",
        vectors_config=models.VectorParams(size=4096, distance=models.Distance.COSINE)
    )

    vector_store = QdrantVectorStore(
    client=client, 
    collection_name="db_schema", 
    embedding=embeddings
    )
    vector_store.add_texts(texts)
    print("✅ Database created and Schema indexed in Qdrant!")

if __name__ == "__main__":
    index_schema()