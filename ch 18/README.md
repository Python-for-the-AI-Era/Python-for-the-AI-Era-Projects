# Project 18: Production LLM API Service

### Overview
This project targets scalable asynchronous web architecture, secure distributed state management, and production-grade LLM gateway engineering. Junior developers use simple client-side scripts to interact with AI frameworks; enterprise platform developers build resilient, secure, high-throughput backend APIs that control costs, enforce security constraints, parse complex data schema layouts, and guarantee predictable execution metrics under significant operational scale.

You will build a professional, asynchronous microservice using **FastAPI** capable of serving streaming chat completions via **Server-Sent Events (SSE)**, structured document analysis, recursive agent tool-calling execution engines, and multi-modal image evaluation. The gateway will be reinforced by asymmetric **JWT verification**, a distributed atomic **Redis sliding-window rate limiter**, and full tracking of API operational costs. The entire cluster is encapsulated using production-ready multi-stage **Dockerfiles** and clean multi-container orchestration environment profiles.

---

### The Architecture Contract

Your implementation must strictly satisfy these cross-platform web microservice blueprints:

#### 1. Non-Blocking Server-Sent Events (`/v1/chat/stream`)
Traditional HTTP REST endpoints fail under heavy language model inference latency because long-lived synchronous connections block worker threads.
* Your chat interface must use an asynchronous generator function wrapped inside FastAPI's native `StreamingResponse`. 
* Output tokens immediately to the network wire using standard SSE syntax strings (`data: {"content": "chunk"}\n\n`).
* **The Telemetry Contract**: The penultimate streaming event message must emit a structured usage dictionary carrying exact token tracking calculations (`total_tokens`), followed immediately by an explicit stream termination signal string (`data: [DONE]\n\n`).

#### 2. Fault-Tolerant Structural Parsing (`/v1/classify`)
When extracting programmatic JSON arrays from raw textual input strings, you cannot afford to pass unstable text blobs down the architectural stack.
* Build strict typing rules using **Pydantic v2 schemas** (defining target severity levels, primary incident classifications, and recommended routing priorities).
* Integrate your system extraction using the `instructor` library to enforce format constraints on the LLM client engine.
* To safeguard your system against transient extraction failures or network anomalies, wrap the execution within a robust loop that attempts up to **3 automated retries** before surfacing an error response.

#### 3. Autonomous Multi-Turn Agent Routing Loops (`/v1/assist`)
Your system helper must implement an autonomous tool execution loop capable of carrying out sequential multi-turn reasoning:
* Register exactly **4 operational tool stubs**: `get_location()`, `get_hospital()`, `send_alert()`, and `check_weather()`.
* If a query commands data requiring external info, your parsing loop must intercept the `tool_calls` parameter dictionary payload, execute the underlying local Python function asynchronously, feed the output back into the message array context history list, and loop back recursively until the language model returns a clean final string response.

#### 4. Real-Time Distributed Performance Guardrails
To defend your API nodes against distributed denial-of-service vectors, protect your cluster via Redis integration:
* **The Authorization Layer**: Do not trust simple plaintext api keys. Secure all entry routes behind asymmetric **JWT Token validation workflows**, extracting authorization signatures via an HTTPBearer dependency mechanism.
* **The Rate Limiter**: Build a sliding-window calculation script using atomic Redis command sets. Track client transactions relative to timestamps, allowing incoming requests only if their current moving-window frequency metrics fit within acceptable traffic ranges.
* **Billing Registries**: Maintain an internal database logging resource usage metrics. Calculate runtime expenses on every transaction based on exact input and output token fee weights, and surface historical cost rollups via an active `GET /v1/billing` endpoint.

#### 5. Multi-Container Orchestration (`docker-compose.yml`)
The platform must scale cleanly and function completely independent of host computer variations:
* Author an optimized, production-ready multi-stage `Dockerfile` to compile your FastAPI environment without shipping unnecessary developer tool footprints.
* Map out your operational dependency network inside a unified `docker-compose.yml` orchestrator configuring three critical environment images: the active FastAPI application engine web gateway, a central **Redis** instance acting as your distributed memory rate-limiter layer, and a robust **PostgreSQL** cluster tracking persistent configuration logs. Include definitive validation check steps (`healthcheck`) on your storage images to ensure components start in the correct sequential order.

---

### Technical Signposts & Hints

#### 1. Formatting Stream Tokens into Valid JSON Strings
When streaming raw tokens over the wire via an active `text/event-stream` interface channel, ensure your inner generator script structure transforms intermediate text components into clean stringified JSON layouts before transmitting them over the socket line. This prevents character truncation or white-space parsing errors inside client-side reader configurations:
```python
# Emitting valid SSE payload segments cleanly
import json
yield f"data: {json.dumps({'content': token_string})}\n\n"

```

#### 2. Resolving Multi-Modal Multi-Part Data Stream Files

When handling high-resolution image uploads via the `/v1/vision` route, ensure your FastAPI parameters utilize an explicit `UploadFile` multi-part reader form object. Read file contents into an asynchronous byte stream array, convert image segments to base64 encoding strings, and pass them downstream to your multi-modal vision model client blocks.

---

### Constraints Checklist

* [ ] No synchronous, blocking `time.sleep()` calls inside your route files; utilize true asynchronous workflows using `await asyncio.sleep()` commands exclusively.
* [ ] The application must launch safely out of the box using a single terminal command: `docker-compose up --build`.
* [ ] System credentials, API tokens, and database authentication variables must be isolated from the codebase, loading securely into production nodes via externalized environmental files (`.env`).
* [ ] Every individual route handler, authentication middleware constructor, schema configuration entity, and utility script block must feature explicit, valid PEP 484 type annotations.

```

---

### Why this works perfectly for Chapter 18:
* **The Asynchronous Reality Shift**: Moving away from legacy synchronous architectures forces you to handle real-world backend engineering realities—like non-blocking network streams, streaming IO, concurrent event queues, and atomic distributed state tracking.
* **The Complete Systems View**: By stitching together FastAPI, Redis, PostgreSQL, Docker, and advanced AI agent execution workflows, you stop viewing AI engineering as an algorithmic modeling puzzle. Instead, you master it as a scalable, high-performance distributed systems engineering domain.

```