import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.utilities import SQLDatabase
#from langchain_community.vectorstores import Qdrant
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

st.set_page_config(page_title="Local SQL AI", layout="wide")
st.title("Text to SQL with Local LLM and Qdrant")

# Connect to the local DB and Services
db = SQLDatabase.from_uri("sqlite:///my_database.db")
llm = OllamaLLM(model="llama3:latest")
embeddings = OllamaEmbeddings(model="llama3:latest")
client = QdrantClient("http://localhost:6333")
#vector_store = Qdrant(client=client, collection_name="db_schema", embeddings=embeddings)
vector_store = QdrantVectorStore(
    client=client, 
    collection_name="db_schema", 
    embedding=embeddings 
)

query = st.text_input("Ask a question about your database:", placeholder="e.g., How many orders does Pratham have?")

if query:
    with st.spinner("Finding tables and writing SQL..."):
        # 1. RAG: Find relevant tables
        relevant_tables = vector_store.similarity_search(query, k=1)
        context = relevant_tables[0].page_content

        # 2. Generate SQL
        prompt = f"Schema: {context}\n\nQuestion: {query}\n\nReturn ONLY the SQL query."
        sql_query = llm.invoke(prompt).strip().replace("```sql", "").replace("```", "")
        
        st.subheader("Generated SQL:")
        st.code(sql_query, language="sql")

        # 3. Run the SQL
        try:
            result = db.run(sql_query)
            st.subheader("Result:")
            st.write(result)
        except Exception as e:
            st.error(f"SQL Error: {e}")