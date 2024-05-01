import requests

def call_llama2_api(prompt, model_name, api_key):
    url = "https://api.example.com/llama2/inference"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "prompt": prompt,
        "parameters": {
            # 可能需要根據文檔提供其他參數
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

api_key = 'none'
model_name = 'llama-2-7b'  # 這裡填寫具體的模型版本，如 Llama-2-7B
prompt = 'What is the weather like today?'

# 調用 API
result = call_llama2_api(prompt, model_name, api_key)
print(result)
