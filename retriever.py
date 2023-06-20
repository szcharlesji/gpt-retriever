import os
import sys
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator

from dotenv import load_dotenv

# Loading API key from .env file
load_dotenv('.env')
api_key = os.getenv('APIKEY')
os.environ["OPENAI_API_KEY"] = api_key

# Get the prompt
query = sys.argv[1]

loader = DirectoryLoader(".", glob="*.txt")
# loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))