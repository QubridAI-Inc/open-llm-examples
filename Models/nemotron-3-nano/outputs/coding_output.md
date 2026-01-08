
## 1. High‑level Architecture Overview  

```
+-------------------+        +-------------------+        +-------------------+
|   Client (HTTP)   |  --->  |   API Gateway /   |  --->  |   LLM Inference   |
|   (browser, CLI) |        |   Load‑Balancer   |        |   Service (Worker)|
+-------------------+        +-------------------+        +-------------------+
                                 |                               |
                                 |                               |
                                 v                               v
                     +-------------------+          +-------------------+
                     |  Rate‑Limiter     |          |  Retry / Circuit  |
                     |  (Redis / In‑mem) |          |  Breaker (Tenacity)|
                     +-------------------+          +-------------------+
                                 |                               |
                                 v                               v
                     +-------------------+          +-------------------+
                     |  Structured Logger|          |  Metrics / Alerts |
                     +-------------------+          +-------------------+

```

| Layer | Responsibility | Typical Tech |
|-------|----------------|--------------|
| **API Gateway / Load‑Balancer** | Terminates TLS, distributes traffic, health‑checks | Nginx, Traefik, AWS ALB, GCP Cloud Load Balancing |
| **FastAPI Service** | HTTP endpoint, request validation, async dispatch | Python 3.11+, FastAPI, Uvicorn/Gunicorn |
| **Rate Limiter** | Enforces per‑IP / per‑API‑key quotas | Redis + `slowapi` or `ratelimit` middleware |
| **Retry / Circuit‑Breaker** | Automatic retries on transient failures, back‑off, fallback | `tenacity` (Python) or Envoy/NGINX retries |
| **LLM Worker** | Executes the heavy inference call (GPU/CPU) | vLLM, HuggingFace `transformers`, TensorRT, or a containerized model server |
| **Structured Logger** | Emits JSON‑structured logs for aggregation & observability | `structlog`, `loguru`, or `python-json-logger` |
| **Metrics & Alerting** | Observability (latency, error rate, queue depth) | Prometheus + Grafana, OpenTelemetry |
| **Persistence (optional)** | Store request‑ids, audit trails, model version | PostgreSQL, DynamoDB, or simple KV store |

---

## 2. Core Design Decisions  

| Concern | Decision | Rationale |
|---------|----------|-----------|
| **Framework** | **FastAPI** (async, automatic OpenAPI docs) | High performance, easy to add middleware, great community support |
| **Rate Limiting** | Token‑bucket stored in **Redis** (shared across replicas) | Works in a horizontally‑scaled deployment; can enforce per‑key, per‑method limits |
| **Retry Logic** | **Tenacity** with exponential back‑off + circuit‑breaker | Simple Pythonic API, can be applied as a decorator to the inference call |
| **Structured Logging** | **structlog** with JSON output | Machine‑readable logs → easy ingestion by Loki, Elasticsearch, Splunk |
| **Scalability** | Deploy as **stateless** FastAPI pods behind a **Kubernetes** Service; LLM inference runs in its own pod (GPU‑enabled) | Horizontal scaling of API layer; inference can be scaled independently (e.g., using GPU node pools) |
| **Configuration** | **pydantic Settings** (environment‑variable driven) | Centralised config, easy to change per‑environment |
| **Testing** | Pytest + `httpx.AsyncClient` for integration tests; contract testing with **Schemathesis** | Guarantees API contract stability |
| **CI/CD** | GitHub Actions → Docker build → push to registry → Helm upgrade | End‑to‑end automation |

---

## 3. Example Code Snippets  

Below are minimal but complete snippets that illustrate each of the required pieces.  
You can copy‑paste them into a fresh repo and run `docker compose up -d` to see everything working locally.

### 3.1 Project Layout  

```
my_llm_service/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point
│   ├── api/
│   │   └── v1.py        # router with /generate endpoint
│   ├── core/
│   │   ├── config.py    # pydantic Settings
│   │   ├── logger.py    # structlog setup
│   │   └── rate_limit.py
│   ├── workers/
│   │   └── inference.py # thin wrapper around the LLM
│   └── middleware/
│       └── request_id.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── k8s/
    └── deployment.yaml
```

### 3.2 `requirements.txt`  

```text
fastapi==0.110.*
uvicorn[standard]==0.27.*
pydantic-settings==2.2.*
structlog==24.1.*
python-json-logger==2.0.*
slowapi==0.1.8          # rate limiting middleware
tenacity==9.0.*
httpx==0.27.*           # for async client in tests
```

### 3.3 Configuration (`app/core/config.py`)  

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Redis (rate limiter)
    redis_url: str = "redis://redis:6379/0"

    # LLM
    model_name: str = "meta-llama/Llama-2-7b-chat-hf"
    max_new_tokens: int = 256
    temperature: float = 0.7

    # Rate limiting
    requests_per_minute: int = 120   # global bucket
    burst_limit: int = 20            # burst size

    # Retry
    max_retries: int = 3
    retry_backoff_factor: float = 0.5

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
```

### 3.4 Structured Logger (`app/core/logger.py`)  

```python
import structlog