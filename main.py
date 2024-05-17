import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from vectordb import Memory
import fitz  # PyMuPDF
from openai import OpenAI

# Read the OpenAI API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize Memory instance from vectordb
memory = Memory()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.), you can specify allowed methods here
    allow_headers=["*"],  # Allows all headers, you can specify allowed headers here
)


class Question(BaseModel):
    question: str


@app.on_event("startup")
def startup_event():
    try:
        if not os.path.exists("documents"):
            os.makedirs("documents")
        load_documents()
    except Exception as e:
        logger.error(f"Error during startup: {e}")


def load_documents():
    documents_folder = "documents"

    for filename in os.listdir(documents_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(documents_folder, filename)
            try:
                text = extract_text_from_pdf(filepath)
                metadata = {"filename": filename}
                memory.save(text, metadata)
                logger.info(f"Ingesting document: {filepath}")
            except Exception as e:
                logger.error(f"Error ingesting document {filepath}: {e}")
    logger.info("Document ingestion complete.")


def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)


def get_relevant_documents(question, top_n=3):
    results = memory.search(query=question, top_n=top_n)
    relevant_texts = [result['chunk'] for result in results]
    return relevant_texts


@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG Pipeline Backend"}


@app.get("/documents")
def get_documents():
    try:
        results = memory.search("", top_n=1000)  # Assuming top_n is large enough to fetch all
        return results
    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        return {"error": str(e)}


@app.post("/ask")
async def ask_question(question: Question):
    try:
        # Retrieve relevant documents from vectordb
        relevant_texts = get_relevant_documents(question.question)

        # Combine the user's question with the retrieved document texts
        combined_prompt = question.question + "\n\n" + "\n".join(relevant_texts)

        # Use GPT-4 to generate an answer
        client = get_openai_client()
        response = client.chat.completions.create(
            model="gpt-4",  # Use the GPT-4 model
            messages=[
                {"role": "user", "content": f"{combined_prompt}"}
            ],
            max_tokens=50
        )

        # Extract and print specific details
        answer = response.choices[0].message.content.strip()

        return {"answer": answer}
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
