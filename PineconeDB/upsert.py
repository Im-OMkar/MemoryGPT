import os
import pinecone
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

from embeddings import get_embeddings

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_INDEX = os.environ.get('PINECONE_INDEX')

# loader = TextLoader('../../../state_of_the_union.txt')
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
embeddings = get_embeddings("first thing to remember")
to_upsert = [{
    "id": "text_1",
    "values": embeddings,
}]

# print("************", embeddings)

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV  # next to api key in console
)

# docsearch = Pinecone.from_documents(docs, embeddings, index_name=PINECONE_INDEX)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

# query = "What did the president say about Ketanji Brown Jackson"
# docs = docsearch.similarity_search(query)

index = pinecone.Index(PINECONE_INDEX)
# index.upsert(to_upsert)
print("**********", index.fetch(['text_1']))
