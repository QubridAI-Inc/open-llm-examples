import requests
import json
from pprint import pprint

url = "https://platform.qubrid.com/api/v1/qubridai/chat/completions"
headers = {
  "Authorization": "Bearer <QUBRID_API_KEY>",
  "Content-Type": "application/json"
}

data = {
  "model": "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16",
  "messages": [
    {
      "role": "user",
      "content": "Explain quantum computing in simple terms"
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200,
  "stream": True,
  "top_p": 1
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Streaming response:")
for line in response.iter_lines():
    if line:
        decoded_line = line.decode("utf-8")
        if decoded_line.startswith("data: "):
            json_str = decoded_line[6:]  # Remove "data: " prefix
            if json_str.strip() == "[DONE]":
                break
            try:
                chunk = json.loads(json_str)
                if "choices" in chunk and len(chunk["choices"]) > 0:
                    content = chunk["choices"][0]["delta"].get("content", "")
                    print(content, end="", flush=True)
            except json.JSONDecodeError:
                continue
