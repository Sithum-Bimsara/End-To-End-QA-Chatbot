# Langchain Chatbot with ChatGroq and Streamlit

This project demonstrates a chatbot powered by Langchain's integration with ChatGroq and OpenAI's embeddings. It allows users to ask questions and receive context-aware answers. The project includes an API built using FastAPI and a Streamlit-based frontend for interaction.

---

## What is Langchain?
Langchain is a framework for developing applications powered by large language models (LLMs). It simplifies interactions with LLMs by providing tools to manage prompts, memory, and workflows. For more details, visit [Langchain's website](https://www.langchain.com).

## What is ChatGroq?
ChatGroq provides a high-performance language model designed for fast and accurate question answering. It offers powerful APIs that integrate seamlessly with Langchain for robust chatbot functionality. For more details, visit [Groq's website](https://www.groq.com).

---

## Features
- **API Integration**: FastAPI backend for handling queries.
- **ChatGroq Integration**: Utilizes Groq's Llama3-8b-8192 model for answering questions.
- **OpenAI Embeddings**: Leverages OpenAI for document embedding and retrieval.
- **Streamlit Frontend**: User-friendly interface for interacting with the chatbot.
- **PDF Support**: Automatically processes documents from a specified directory for context-aware answering.

---

## Project Structure
```
langchain-chatgroq/
|
├── api/
│   ├── app.py                # FastAPI app with ChatGroq
│   └── client.py             # Streamlit client for user interaction
├── data/
│   └── us_census/            # Directory containing PDF documents for embeddings
├── requirements.txt          # List of dependencies
├── .env                      # Environment variables for API keys
└── README.md                 # Project documentation
```

---

## Prerequisites
Before starting, ensure the following are installed:

- **Python** (3.7 or higher)
- **pip** (Python package installer)
- **Groq** (For Llama3-8b-8192 model)
- **FAISS** (For efficient similarity search)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sithum-Bimsara/Langchain-ChatGroq.git
cd Langchain-ChatGroq
```

### 2. Create a Virtual Environment
- On Windows:
  ```bash
  python -m venv venv
  ```
- On macOS/Linux:
  ```bash
  python3 -m venv venv
  ```

### 3. Activate the Virtual Environment
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```
OPENAI_API_KEY="your_openai_api_key"
GROQ_API_KEY="your_groq_api_key"
```
Replace the placeholders with your actual API keys.

### 6. Run the Backend
To start the FastAPI backend:
```bash
uvicorn api.app:app --reload --host localhost --port 8000
```

### 7. Run the Frontend
In another terminal, start the Streamlit frontend:
```bash
streamlit run api/client.py
```
The app will be accessible in your browser at [http://localhost:8501](http://localhost:8501).

---

## Usage
1. **Ask a Question**:
   - Enter a question in the Streamlit input box.
   - Click the "Ask" button.

2. **View Answer and Context**:
   - The chatbot will display an answer along with the relevant context extracted from the documents in the `us_census/` folder.

---

## Requirements
The dependencies for this project are listed in `requirements.txt`. Some key packages include:

- `fastapi>=0.100.0`
- `streamlit>=1.24.0`
- `langchain-core>=0.0.1`
- `langchain-groq>=0.0.1`
- `langchain-community>=0.0.1`
- `faiss-cpu>=1.7.4`
- `python-dotenv>=1.0.0`

Install them using:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting
- **Invalid API Keys**: Ensure `.env` contains valid keys for OpenAI and Groq.
- **Missing Dependencies**: Run `pip install -r requirements.txt` to resolve missing packages.
- **File Loading Issues**: Ensure the `us_census` folder contains valid PDF files.

---

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

