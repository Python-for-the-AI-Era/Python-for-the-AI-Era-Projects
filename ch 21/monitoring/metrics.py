from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Response

# --- PROMETHEUS METRIC REGISTRIES ---

LLM_REQUESTS_TOTAL = Counter(
    "llm_requests_total", 
    "Total volume of incoming LLM gateway requests", 
    ["endpoint", "model_version", "status_code"]
)

LLM_LATENCY_SECONDS = Histogram(
    "llm_latency_seconds", 
    "Distribution tracking of structural LLM request execution latencies", 
    ["endpoint", "model_version"],
    buckets=(0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, float("inf"))
)

ACTIVE_STREAMING_CONNECTIONS = Gauge(
    "active_streaming_connections",
    "Current volume of parallel ongoing SSE text connection streams"
)

def instrument_app_routing(app: FastAPI):
    """
    TODO: Build an active middleware interceptor loop that tracks incoming 
    requests, measures system delta times, increments appropriate counters, 
    and handles route registrations for a public exposed /metrics extraction endpoint.
    """
    @app.get("/metrics", tags=["Infrastructure"])
    def metrics_endpoint():
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)