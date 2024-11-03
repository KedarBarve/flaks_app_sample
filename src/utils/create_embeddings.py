from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModel
import torch

mongo_connection_string = "CONN_STRING"
MONGO_DB = "mongo_vector_search_sandesh"
SOURCE_COLLECTION = "company"
TARGET_COLLECTION = "company_embeddings"

# Connect to MongoDB
client = MongoClient(mongo_connection_string)  # Replace with your MongoDB URI
db = client[MONGO_DB]
source_collection = db[SOURCE_COLLECTION]
target_collection = db[TARGET_COLLECTION]

# Load a pre-trained Hugging Face model for embeddings
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # You can use any model you prefer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


# Function to generate embeddings
def get_embeddings(text):
    try:
        inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        # Pool the output into a single embedding (you can customize this step)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return embeddings
    except:
        return None


# Fetch the document and create embeddings
def create_and_save_embeddings():
    # Fetch all documents from the source collection
    count = 0
    for document in source_collection.find():
        count = count + 1
        name = document.get('company_name')  # Replace with the actual field name
        desc = str(document.get('company_description'))  # Replace with the actual field name
        if name:
            # Generate embeddings
            name_embedding = get_embeddings(name)
            if desc is None:
                desc = ' '
            desc_embedding = get_embeddings(desc)

            # Save to the target collection
            target_document = {
                'source_document_id': document['_id'],  # Reference to the original document
                'company_name': name,  # Store the original text if needed
                'company_description': desc,  # Store the original text if needed
                'company_name_embedding': name_embedding.tolist(),  # Save embeddings as a list
                'company_description_embedding': desc_embedding.tolist()  # Save embeddings as a list
            }
            target_collection.insert_one(target_document)
            print(f"Saved embedding for document ID: {document['_id']}")

        # if count > 5:
        #     break


# Call the function to create embeddings and save to MongoDB
create_and_save_embeddings()
