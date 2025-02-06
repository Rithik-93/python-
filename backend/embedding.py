import google.generativeai as genai
from configs import config 

gemini_api_key = config.GEMINI
genai.configure(api_key=gemini_api_key)

def generateEmbedding(text: str):
    result = genai.embed_content(
    model="models/text-embedding-004", content=text, output_dimensionality=768
    )
    return result["embedding"]





# import json
# import requests
# from configs import config

# key = config.KEY

# headers = {"Authorization": f"Bearer {key}"}

# url = "https://api.edenai.run/v2/text/embedding"  # Replace with actual feature/subfeature
# payload = {
#     "providers": "openai",  # Example provider
#     "text": "What is the meaning of life?",
#     "language": "en"
# }

# response = requests.post(url, json=payload, headers=headers)

# # Debugging: Print response content
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)

# # Check if response is valid JSON
# try:
#     result = response.json()  # Use .json() instead of json.loads(response.text)
#     print(result)
# except json.JSONDecodeError:
#     print("Invalid JSON response received!")
