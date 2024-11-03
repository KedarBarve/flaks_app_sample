import requests
import base64
import json
from requests.auth import HTTPDigestAuth
from pymongo import MongoClient

# MongoDB Atlas project details
public_key = 'yxjoweqw'  # Replace with your MongoDB Atlas API Public Key
private_key = 'c46c5247-e139-423a-9d57-8ff5f2596183'  # Replace with your MongoDB Atlas API Private Key
project_id = '637b0f3b3fe4d22e0b7887ee'  # Replace with your MongoDB Atlas Project ID
cluster_name = 'cluster-dev'  # Replace with your MongoDB Atlas Cluster Name
database_name = 'mongo_vector_search_sandesh'  # Replace with your Database Name
collection_name = 'company'  # Replace with your Collection Name
fulltext_search_index = 'company_fulltext_index'  # Replace with your Collection Name


# Create basic authentication header for API request
auth = f"{public_key}:{private_key}"
encoded_auth = base64.b64encode(auth.encode('utf-8')).decode('utf-8')

# API endpoint for creating an Atlas Search Index
url = f"https://cloud.mongodb.com/api/atlas/v2/groups/{project_id}/clusters/{cluster_name}/search/indexes?pretty=true"

# Define the search index configuration (customize based on your use case)
index_config = {
    "collectionName": collection_name,
    "database": database_name,
    "name": fulltext_search_index,  # The name of your index
    "definition": {
        "mappings": {
            "dynamic": False,  # Automatically indexes all fields
            "fields": {
                "company_name": {
                    "type": "string"
                }
            }
        }
    }
}

# Send the request to create the search index
headers = {
    'Authorization': f'Basic {encoded_auth}',
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.atlas.2024-05-30+json'
}

response = requests.post(url, headers=headers, auth=HTTPDigestAuth(public_key, private_key), data=json.dumps(index_config))

# Check if the index was created successfully
if response.status_code == 201:
    print(f"Search index created successfully: {response.json()}")
else:
    print(f"Failed to create search index: {response.status_code} - {response.text}")

