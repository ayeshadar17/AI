import requests

API_URL = "https://router.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": "Bearer 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"
}

payload = {
    "inputs": "I love this product!",
    "options": {"wait_for_model": True}
}

response = requests.post(API_URL, headers=headers, json=payload)

print(response.status_code)
print(response.json())


