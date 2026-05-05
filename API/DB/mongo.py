from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()



MONGO_URI= os.getenv('MONGO_URI')

if not MONGO_URI:
    raise ValueError("MONGO_URI not found in environment variables")

client = MongoClient(MONGO_URI)


db = client["research_assistant"]
chat_collection = db["chats"]


chat_collection.create_index("thread_id", unique=True)