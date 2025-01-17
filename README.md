# Langchain Chatbot with ChatGroq and Streamlit

This project demonstrates a chatbot powered by Langchain's integration with ChatGroq and OpenAI's embeddings. It allows users to ask questions and receive context-aware answers. The project includes an API built using FastAPI and a Streamlit-based frontend for interaction.

---

## What is Streamlit?
Streamlit is an open-source app framework used to build interactive web applications with Python. It's particularly useful for creating data applications and machine learning demos, allowing developers to quickly prototype and deploy apps.

For more details, visit [Streamlit's website](https://streamlit.io/) _(opens in a new tab)_.

---

## What is Langchain?
Langchain is a framework for developing applications powered by large language models (LLMs). It simplifies interactions with LLMs by providing tools to manage prompts, memory, and workflows. For more details, visit [Langchain's website](https://www.langchain.com).

---

## What is Groq?
Groq represents a paradigm shift in AI inference, enabling instant intelligence for developers and enterprises. Its highlights include:

- **The Groq Language Processing Unit (LPU)**: A hardware solution designed specifically for AI inference and language tasks, offering unparalleled speed, affordability, and scalability.
- **Cloud and on-premises availability**: Users can access Groq’s capabilities via GroqCloud™ or deploy LPUs in on-premise AI compute centers.
- **Energy efficiency**: Groq’s design focuses on delivering maximum performance while minimizing energy consumption.

Groq is committed to democratizing AI by making its technology accessible to everyone.

For more details, visit [Groq's website](https://groq.com/) _(opens in a new tab)_.



## Usage of Groq in This Project
In this project, Groq’s **LPU** is leveraged to power the inference engine for the ChatGroq API. This ensures:

1. **Fast AI inference**: Rapid and responsive user interactions.
2. **Scalability**: Support for complex and high-volume queries.
3. **Energy efficiency**: Reduced resource consumption compared to traditional inference methods.


---

## What is FastAPI?
FastAPI is a modern, fast, and high-performance web framework for building APIs with Python. It is designed for ease of use, developer productivity, and fast execution, making it a great choice for creating robust RESTful APIs. Built on standard Python type hints, FastAPI provides automatic data validation, interactive API documentation (via Swagger and ReDoc), and asynchronous capabilities powered by ASGI.

For more details, visit [FastAPI's official documentation](https://fastapi.tiangolo.com/#installation)

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
End-To-End-QA-Chatbot/
|
├── groq/
│   ├── app.py                # FastAPI app with ChatGroq
│   └── client.py             # Streamlit client for user interaction
│   └── us_census             # Directory containing PDF documents for embeddings
│   
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
git clone https://github.com/Sithum-Bimsara/End-To-End-QA-Chatbot.git
cd End-To-End-QA-Chatbot.git
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
cd groq
uvicorn api.app:app --reload --host localhost --port 8000
```

### 7. Run the Frontend
In another terminal, start the Streamlit frontend:
```bash
cd groq
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

- `fastapi`
- `streamlit`
- `langchain-core`
- `langchain-groq`
- `langchain-community`
- `faiss-cpu`
- `python-dotenv0`

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

