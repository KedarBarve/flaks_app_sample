from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

mongo_connection_string = "CONNECTION_STRING"
cluster_name = 'CLUSTER_NAME'  # Replace with your MongoDB Atlas Cluster Name
# database_name = 'mongo_vector_search_sandesh'  # Replace with your Database Name
database_name = 'DB_NAME'  # Replace with your Database Name
# collection_name = 'company_exhibitor_detail'  # Replace with your Collection Name
collection_name = 'COLLECTION_NAME'  # Replace with your Collection Name


def read(srch_phrase):
    client = MongoClient(mongo_connection_string)

    # Connect to your specific database and collection
    db = client[database_name]
    collection = db[collection_name]

    print("collection: " + str(collection))

    query = {}

    documents = collection.find(query)

    for doc in documents:
        vector_field = doc.get("name_embedding", None)
        if vector_field:
            print(f"Document ID: {doc['_id']} - Vector Field: {vector_field}")
        else:
            print(f"Document ID: {doc['_id']} - No vector field found")


read("aperion_user")
