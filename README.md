# RAG Pipeline Project

## Introduction

The RAG (Retrieval-Augmented Generation) Pipeline Project is a web application designed to answer questions based on the content of PDF documents. The system uses FastAPI to handle API requests, VectorDB to manage and search document contents, and the OpenAI API to generate responses.

## Features

- **Document Ingestion**: Load PDF documents, extract text, and store it in VectorDB.
- **Question Answering**: Retrieve relevant document texts based on user queries and generate answers using OpenAI's GPT-4 model.
- **Interactive UI**: User-friendly frontend to submit questions and display answers with a loading animation.

## Requirements

To run this project, you will need the following software and dependencies:

- **Python**: Version 3.7 or higher
- **Pip**: Python package installer
- **Necessary Libraries**:
  - `fastapi`: For building the API
  - `uvicorn`: For running the ASGI server
  - `pydantic`: For data validation and settings management
  - `vectordb2`: For managing and searching document contents
  - `openai`: For interacting with the OpenAI API
  - `pymupdf`: For extracting text from PDF files
- **Web Browser**: For accessing the frontend interface

## Installation

1. **Clone the Repository**:
   
   ```sh
   git clone https://github.com/rhemanthk93/RAG.git
   cd rag
   
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt

3. **Download SpaCy Language Model**:
   ```sh
   python -m spacy download en_core_web_sm

4. **Set the OpenAI API Key**:
   ```sh
   set OPENAI_API_KEY=your_openai_api_key
   export OPENAI_API_KEY=your_openai_api_key
   
5. **Run the Backend**
   ```sh
   uvicorn main:app --reload

6. **Run the Frontend**
   ```sh
   python -m http.server 8001

## Endpoints

### `GET /`
- **Description**: Root endpoint to check if the server is running.
- **Response**: 
  ```json
  {
    "message": "Welcome to the RAG Pipeline Backend"
  }

### `GET /documents`
- **Description**: Fetches all stored documents..
- **Response**: 
  ```json
  [
    {
      "chunk": "Text from document...",
      "metadata": {
        "filename": "document1.pdf"
      }
    },
    {
      "chunk": "Text from another document...",
      "metadata": {
        "filename": "document2.pdf"
      }
    }
  ]

### `POST /ask`
- **Description**: Accepts a question and returns an answer generated using GPT-4.
- **Request Body**: 
  ```json
  {
    "question": "Enter your question here"
  }
- **Response**: 
  ```json
  {
    "answer": "Generated answer based on the documents and question."
  }

## Potential Questions

- What is the nature of the lawsuit between Ace Decade Holdings Limited and UBS AG?
- What misrepresentations and deceptions did UBS allegedly commit against Ace Decade?
- How did UBS's advice influence Ace Decade's investment decisions?
- What were the terms and implications of the Financing Letter and margin call provisions?
- How did the involvement of Haixia as an intermediary impact Ace Decade's investment?
- What were the consequences of the margin call issued by UBS in July 2015?
- How did UBS benefit financially from the sale of Ace Decade's Haitong shares?
- What are the specific allegations made by Ace Decade against UBS in terms of breach of fiduciary duty?
- What damages is Ace Decade seeking from UBS in this lawsuit?
- What role did Haixia play in the loan financing agreement with UBS?
- How did the relationship between UBS and Haixia affect Ace Decade's interests?
- What were the results of the block trade executed by UBS for Ace Decade's Haitong shares?
- How did UBS allegedly fail to cooperate with Ace Decade during the margin call event?
- What is the basis for Ace Decade's claims of common law fraud and constructive fraud against UBS?
- What were the financial losses incurred by Ace Decade as a result of UBS's actions?


