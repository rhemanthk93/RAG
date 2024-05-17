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
  - `python-multipart`: For handling form data (optional, but often used with FastAPI)
  - `vectordb2`: For managing and searching document contents
  - `openai`: For interacting with the OpenAI API
  - `pymupdf`: For extracting text from PDF files
  - `spacy`: For natural language processing tasks
- **Web Browser**: For accessing the frontend interface

## Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/rhemanthk93/RAG.git
   cd rag
   
2. **Install Dependencies**:
   pip install -r requirements.txt

3. **Download SpaCy Language Model**:
   python -m spacy download en_core_web_sm

4. **
