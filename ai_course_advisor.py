import requests
import json
import os
from dotenv import load_dotenv

# Load API key from .env file (recommended)
load_dotenv()
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")

# Watsonx endpoint and headers
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text-generation"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Prompt input
user_input = "I want to become a Cybersecurity Analyst. Give me a detailed 6-month roadmap with tools, certifications, and platforms."

# Payload structure
payload = {
    "model_id": "granite-13b-chat-v2",
    "input": user_input,
    "parameters": {
        "decoding_method": "sample",
        "max_new_tokens": 1024,
        "min_new_tokens": 200,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1
    },
    "project_id": PROJECT_ID
}

# Send request
response = requests.post(url, headers=headers, json=payload)

# Parse and display result
if response.status_code == 200:
    result = response.json()
    print("\n--- LearnMate Roadmap ---\n")
    print(result['results'][0]['generated_text'])
else:
    print("Error:", response.status_code)
    print(response.text)
