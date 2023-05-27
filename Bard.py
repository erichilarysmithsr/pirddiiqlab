import requests

headers = { 'Authorization': 'Bearer acec4077-d5ad-4a48-863a-f3c9cc06563a', 'Content-Type': 'text/plain' }
data = { "input": "Who won the world cup last year?" }
req = requests.post('http://localhost:4000/chat', headers=headers, json=data)
print(req.json())
