import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

def ask_question(question):
    response = requests.post(
        f"{API_BASE_URL}/ask",
        json={"question": question}
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Streamlit UI
st.title("Langchain ChatGroq Client")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question:
        response = ask_question(question)
        st.write("Answer:")
        st.write(response.get("answer", "No answer found."))
        
        with st.expander("Relevant Context"):
            for context in response.get("context", []):
                st.write(context)
                st.write("-------------------")
