import requests
import base64
import json
from requests.auth import HTTPDigestAuth
from pymongo import MongoClient

# MongoDB Atlas project details
public_key = 'PUBLIC_KEY'  # Replace with your MongoDB Atlas API Public Key
private_key = 'PRIVATE_KEY'  # Replace with your MongoDB Atlas API Private Key
project_id = 'PROJECT_ID'  # Replace with your MongoDB Atlas Project ID
cluster_name = 'CLUSTER_NAME'  # Replace with your MongoDB Atlas Cluster Name
database_name = 'DB_NAME'  # Replace with your Database Name
collection_name = 'COLLECTION_NAME'  # Replace with your Collection Name
my_search_index = 'SEARCH_INDEX'  # Replace with your Collection Name

# Create basic authentication header for API request
auth = f"{public_key}:{private_key}"
encoded_auth = base64.b64encode(auth.encode('utf-8')).decode('utf-8')

# API endpoint for creating an Atlas Search Index
url = f"https://cloud.mongodb.com/api/atlas/v2/groups/{project_id}/clusters/{cluster_name}/search/indexes?pretty=true"

# Define the search index configuration (customize based on your use case)
index_config = {
    "collectionName": collection_name,
    "database": database_name,
    "name": my_search_index,  # The name of your index
    "definition": {
        "mappings": {
            "dynamic": False,  # Automatically indexes all fields
            "fields": {
                "user": {
                    "type": "string"
                }
                # ,
                # "company_description": {
                #     "type": "string"
                # },
                # You can define more fields here with different types, like number, date, etc.
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

