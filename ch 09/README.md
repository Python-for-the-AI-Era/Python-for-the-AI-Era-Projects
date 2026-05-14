# Project 09: Framework Comparison Benchmark

### Overview
This capstone project is an architectural engineering challenge. Instead of debating the syntax of Python web frameworks, you will build, containerize, route, and load-test the exact same CRUD API spec across three completely different design ecosystems: **FastAPI** (Asynchronous ASGI), **Flask** (Minimal WSGI), and **Django REST Framework** (Batteries-Included Monolithic WSGI).

You will run a production simulation using `docker-compose`, map microservice paths behind an `Nginx` reverse proxy, and write an end-to-end load profile with `Locust` to capture objective empirical performance data.

---

### The Architecture Contract

Your multi-service network must satisfy these explicit deployment and validation requirements:

#### 1. Unified Nginx Routing Context
You will deploy a single entrance gateway. Your API services must not expose raw network ports directly to the host machine. Instead, configure an `nginx.conf` routing grid to parse incoming paths and handle upstream proxy passing:
* `http://localhost/fastapi/users` -> Routes internally to `fastapi_api:8000`
* `http://localhost/flask/users`   -> Routes internally to `flask_api:5000`
* `http://localhost/django/users`  -> Routes internally to `django_api:8000`

#### 2. Matrix Testing via Parametrization
Do not write separate test folders for each framework. You must implement a single `pytest` suite inside the `shared_tests/` folder.
* Utilize `pytest` parametrization hooks to loop your test logic dynamically across all three framework URLs. This ensures that your validation standards—such as field validation structures and error payloads—remain perfectly identical across every implementation.

#### 3. Database Pre-Seeding (`conftest.py`)
To ensure your benchmarks measure actual query performance and JSON parsing under realistic scale rather than hitting an empty table, your `conftest.py` setup must execute a pre-test routine:
* Programmatically insert **10,000 mock user rows** into the shared PostgreSQL database before Locust begins executing its load profiles.

#### 4. The Performance Stress Baseline
Configure a `locustfile.py` script to simulate real-world request stress. Run a 60-second test simulating **100 concurrent users** hitting your endpoints continuously. Your final report must document and compare the following performance data:
* Maximum throughput ceiling (**Requests Per Second**)
* Latency percentiles (**p50, p95, and p99 distribution ranges**)
* Fault rates under pressure (**Error Percentages**)

---

### Technical Signposts & Hints

#### 1. Configuring Path Striping in Nginx
When Nginx catches an incoming request path like `/fastapi/users`, passing that string directly to FastAPI will result in a `404 Not Found` unless your code explicitly expects the prefix. Use the Nginx `rewrite` directive inside your location blocks to cleanly strip away the framework routing tag before forwarding the traffic downstream:
```nginx
location /fastapi/ {
    rewrite ^/fastapi/(.*)$ /$1 break;
    proxy_pass http://fastapi_api:8000;
}

```

#### 2. Managing WSGI Concurrency (Gunicorn)

Unlike FastAPI, which manages multiple concurrent requests natively on a single thread using its asynchronous event loop, Flask and Django are synchronous WSGI apps. If you boot them using a single runtime process, they can only handle one incoming request at a time, causing their latency metrics to skyrocket during the load test.

* **Signpost**: Configure your Dockerfile execution commands to run Flask and Django behind **Gunicorn**, spawning a minimum of **4 active worker processes** (`gunicorn -w 4 -b 0.0.0.0:5000 app:app`) to distribute the incoming traffic across multiple CPU threads.

---

### Constraints Checklist

* [ ] Every endpoint across all three frameworks must read from and write to the same central PostgreSQL database instance.
* [ ] No third-party plugins or quick-start app wrappers can be used for the base configurations. All app instantiations must use native initialization blocks.
* [ ] The input payloads for POST/PUT operations must enforce strict data rules (e.g., proper email structure and string length limits) using the framework's native tools (Pydantic for FastAPI, Marshmallow/WTForms for Flask, Serializers for DRF).
* [ ] All code directories must include a clean, optimized `Dockerfile` leveraging multi-stage layer patterns to minimize target production footprint sizing.

```

---

### Why this works perfectly for Chapter 09:
* **The Asynchronous Realization**: When students look at the Locust chart and see FastAPI processing 1,800+ requests/sec at single-digit latencies while WSGI frameworks plateau around 400 requests/sec, they immediately understand the architectural reason for choosing **async ASGI stacks** for high-concurrency systems.
* **The Operational Reality Check**: Conversely, they will see that setting up user validation, routing, database management, and administrative dashboards takes an afternoon in Django but can take days to assemble manually from scratch in Flask or FastAPI. This underscores the true lesson of backend design: **choosing the right tool is a balance of execution speed versus developer velocity**.

```