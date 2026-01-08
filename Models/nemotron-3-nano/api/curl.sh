curl -X POST "https://platform.qubrid.com/api/v1/qubridai/chat/completions" \
  -H "Authorization: Bearer <QUBRID_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16",
  "messages": [
    {
      "role": "user",
      "content": "Explain quantum computing in simple terms"
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200,
  "stream": true,
  "top_p": 1
}'