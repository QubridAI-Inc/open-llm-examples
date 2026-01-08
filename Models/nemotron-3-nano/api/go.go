package main

import (
  "bytes"
  "encoding/json"
  "net/http"
)

func main() {
  url := "https://platform.qubrid.com/api/v1/qubridai/chat/completions"

  data := {
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
}
  jsonData, _ := json.Marshal(data)

  req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
  req.Header.Set("Authorization", "Bearer <QUBRID_API_KEY>")
  req.Header.Set("Content-Type", "application/json")

  client := &http.Client{}
  res, _ := client.Do(req)
}