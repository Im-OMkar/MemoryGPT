import os
import openai
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def get_embeddings(text: str, model="text-embedding-ada-002") -> list[float]:
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]
