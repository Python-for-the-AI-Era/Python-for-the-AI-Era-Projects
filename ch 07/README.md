# Project 07: Async Multi-Source News Aggregator

### Overview
This project challenges you to coordinate multi-source non-blocking network requests concurrently. In a production environment, sequential web crawling is highly inefficient due to network lag. You will leverage asynchronous workflows using `asyncio` and `httpx` to build a real-time news aggregation pipeline that fetches data in parallel, deduplicates incoming vectors, and scores results algorithmically.

---

### The Architecture Contract

Your implementation must accurately reflect these core architectural rules:

#### 1. Coordinated Gathering (`asyncio.gather`)
You must execute your individual fetch networks in parallel. Do not await tasks sequentially. Use `asyncio.gather()` to collapse wait times down to the duration of the slowest single endpoint response.
* **HackerNews Fan-Out**: The HackerNews API requires a two-step retrieval process. You must first fetch the array of top integer IDs, slice the top 30, and then spin up 30 secondary *sub-tasks* nested inside a secondary `asyncio.gather()` loop using your shared `httpx.AsyncClient` session.

#### 2. The Title Fingerprint Deduplicator
News items shared across multiple aggregators must be filtered immediately. 
* To do this safely without direct string match breakdowns, isolate the first 5 words of every incoming title string, strip trailing text markers, normalize them to lowercase, and construct a stable integer or string hash fingerprint. Use a local execution `set` to intercept incoming collisions.

#### 3. Logarithmic Scaling and Time Decay Logic
To determine structural placement in your terminal UI output table, every single distinct news document entity must resolve to a calculated dynamic score using this explicit formula:
$$\text{Final Score} = \text{Recency Score} \times \text{Engagement Score} \times \text{Source Weight}$$

* **Recency Component**: $\frac{1}{\text{hours\_since\_published} + 1}$
* **Engagement Component**: $\log(1 + \text{votes})$ (Use `math.log` or `math.log1p`)

---

### Technical Signposts & Hints

#### 1. Designing HTTP Session Context Managers
Never instantiate independent `httpx.AsyncClient()` nodes inside nested operational loops; opening and closing TLS network sockets repeatedly introduces massive performance penalties. 
* Use a single client as an overarching async context manager at the start of your runtime orchestrator, passing its object reference downward as a parameter:
```python
async with httpx.AsyncClient(timeout=5.0) as client:
    # Pass this active client down to child fetch routines
    hn_stories = await fetch_hackernews(client)

```

#### 2. Bonus Challenge: Continuous Async Interleaving

To integrate the Binance real-time WebSockets tracking ticker alongside your text dashboard pipelines, you must spawn a persistent background task. Use `asyncio.create_task()` to start the WebSocket connection loop, allowing it to share execution time concurrently with your network request operations without blocking your main application loop:

```python
# Launch non-blocking background network socket routine
ticker_task = asyncio.create_task(binance_websocket_stream())

```

---

### Constraints Checklist

* [ ] No uses of the blocking `requests` library; all endpoints must leverage asynchronous `httpx` wrappers.
* [ ] Explicit error handling catch policies binding `httpx.TimeoutException` or bad HTTP statuses, preventing single-site crashes from breaking the whole loop.
* [ ] The terminal display print layout output must format scores to 2 decimal points and cap titles strictly at 70 characters with ellipses.
* [ ] Final aggregated records list outputs must export cleanly as parsed standard `json` configurations to disk.

```

---

### Why this works perfectly for Chapter 07:
* **The HackerNews Fan-Out Challenge**: Forcing them to execute a list comprehension of 30 async tasks inside an `asyncio.gather` context completely solidifies how concurrency scales horizontally.
* **Logarithmic Weight Scaling**: Introducing logarithmic scoring (`math.log`) ensures that a story with 10,000 votes doesn't completely bury a fresh story with 10 votes, combining real-world data science metrics with asynchronous engineering.

```