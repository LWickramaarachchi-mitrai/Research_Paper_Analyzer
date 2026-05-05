from pymongo import MongoClient
import os
MONGO_URI = "mongodb+srv://linwick679_db_user:x6pF9Zg99xWZf5Ky@cluster0.kuu5v5r.mongodb.net/research_rag?retryWrites=true&w=majority"

if not MONGO_URI:
    raise ValueError("MONGO_URI not found in environment variables")

client = MongoClient(MONGO_URI)


db = client["research_assistant"]
chat_collection = db["chats"]


chat_collection.create_index("thread_id", unique=True)