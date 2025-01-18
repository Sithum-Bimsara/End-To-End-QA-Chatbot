
from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize API keys
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

# FastAPI app initialization
app = FastAPI(
    title="Langchain API with ChatGroq",
    description="API to handle ChatGroq and Llama3 queries",
    version="1.0"
)

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Initialize prompt template
prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

# Define request models
class EmbeddingRequest(BaseModel):
    question: str

# Initialize vector embeddings globally
vectors = None
retriever = None

@app.on_event("startup")
async def load_embeddings():
    global vectors, retriever
    embeddings = OpenAIEmbeddings()
    loader = PyPDFDirectoryLoader("./us_census") 
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs[:20])
    vectors = FAISS.from_documents(final_documents, embeddings)
    retriever = vectors.as_retriever()


@app.post("/ask")
async def answer_question(request: EmbeddingRequest):
    global retriever
    document_chain = create_stuff_documents_chain(llm, prompt_template)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'input': request.question})
    return {"answer": response['answer'], "context": [doc.page_content for doc in response['context']]}

