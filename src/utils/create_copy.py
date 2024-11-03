from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModel
import torch

mongo_connection_string = "CONNECTION_STRING"
MONGO_DB="mongo_vector_search_sandesh"
SOURCE_COLLECTION="company_exhibitor_detail"
TARGET_COLLECTION="company"


# Connect to MongoDB
client = MongoClient(mongo_connection_string)  # Replace with your MongoDB URI
db = client[MONGO_DB]
source_collection = db[SOURCE_COLLECTION]
target_collection = db[TARGET_COLLECTION]



# Fetch the document and create embeddings
def create_and_save_embeddings():
    # Fetch all documents from the source collection
    count = 0
    for document in source_collection.find():
        target_collection.insert_one(document)
        print(f"Saved embedding for document ID: {document['_id']}")



# Call the function to create embeddings and save to MongoDB
create_and_save_embeddings()
