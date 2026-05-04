from DB.mongo import chat_collection
from datetime import datetime


def save_message(thread_id: str, role: str, content: str):
    chat_collection.update_one(
        {"thread_id": thread_id},
        {
            "$push": {
                "messages": {
                    "role": role,
                    "content": content,
                    "timestamp": datetime.utcnow()
                }
            },
            "$set": {"updated_at": datetime.utcnow()},
            "$setOnInsert": {
                "created_at": datetime.utcnow(),
                "thread_id": thread_id
            }
        },
        upsert=True
    )


def get_chat_history(thread_id: str):
    doc = chat_collection.find_one({"thread_id": thread_id})

    if not doc:
        return []

    return doc["messages"]


def get_all_threads():
    threads = chat_collection.find({}, {"thread_id": 1, "_id": 0})
    return [t["thread_id"] for t in threads]


def delete_thread(thread_id: str):
    chat_collection.delete_one({"thread_id": thread_id})