const body = {
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
};

const res = await fetch("https://platform.qubrid.com/api/v1/qubridai/chat/completions", {
  method: "POST",
  headers: {
    Authorization: "Bearer <QUBRID_API_KEY>",
    "Content-Type": "application/json"
  },
  body: JSON.stringify(body)
});

const result = await res.json();