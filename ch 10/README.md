# Project 10: Async Concurrency Visualiser

### Overview
This project serves as an empirical verification of Python's single-threaded event loop architecture. Instead of just reading about non-blocking code, you will build a diagnostic micro-benchmarking tool that measures wall-clock execution times across three distinct execution design paths: **Serial Execution**, **Unbounded Concurrent Gathering**, and **Rate-Limited Concurrent Task Groups**.

By adjusting tasks, base network simulation delay thresholds, and random execution noise (jitter), you will calculate exact speedup multipliers and observe firsthand how Python scales under I/O heavy load.

---

### The Architecture Contract

Your implementation must strictly fulfill these asynchronous scheduling rules:

#### 1. Real Elapsed Time via `time.perf_counter()`
When measuring programmatic duration loops, never rely on standard `time.time()`. System clock synchronization changes can skew real results. 
* **The Rule**: You must benchmark your orchestration blocks using `time.perf_counter()`. This provides a high-resolution monotonic timer specifically designed for measuring brief execution differentials:
  ```python
  start = time.perf_counter()
  # Execute asynchronous operation...
  elapsed_ms = (time.perf_counter() - start) * 1000

```

#### 2. Traditional Gathering (`asyncio.gather`)

Your second benchmark must trigger all tasks in parallel without any pool limits. Use a list comprehension to instantiate the task coroutines, unpack them into `asyncio.gather(*tasks)`, and verify that the final wall-clock duration matches the single longest sleeping task rather than the sum of all tasks.

#### 3. Modern Structural Concurrency (`asyncio.TaskGroup`)

Python 3.11 introduced `asyncio.TaskGroup` as a safer, more robust interface for managing batches of concurrent tasks. If a single task inside a `TaskGroup` raises an exception, all other active tasks in the group are automatically cancelled, preventing floating, untracked coroutine leaks.

* **The Rule**: Your third benchmark must use the modern `async with asyncio.TaskGroup() as tg:` context manager syntax. Instead of pre-building a coroutine array, you must explicitly spawn tasks onto the loop using:
```python
tg.create_task(coroutine)

```



#### 4. Protecting Resources via `asyncio.Semaphore`

Spawning 10,000 unbounded concurrent tasks against a real database or target microservice can exhaust socket pools, trigger rate limits, or crash remote servers.

* To control concurrency limits within your `TaskGroup` workflow, you must implement a rate-limiting `asyncio.Semaphore(max_concurrent)`.
* Tasks must capture a slot via `async with semaphore:` before initializing their simulated `asyncio.sleep` work cycle.

---

### Technical Signposts & Hints

#### 1. Calculating the Jitter Variable Matrix

When generating execution noise to mimic volatile real-world API latencies, calculate your random bounding limits cleanly using Python's native `random.uniform(a, b)`. Ensure your duration math values account for variations correctly:

```python
min_bound = base_duration - jitter
max_bound = base_duration + jitter
actual_delay_ms = random.uniform(min_bound, max_bound)

```

#### 2. Evaluating the Speedup Coefficient Factor

The speedup multiplier represents the exact performance gain achieved by choosing a concurrent architecture over sequential execution. Compute and format this value by dividing your recorded baseline serial wall-clock metrics by your concurrent test duration results:


$$\text{Speedup Factor} = \frac{\text{Serial Duration (ms)}}{\text{Concurrent Duration (ms)}}$$

* Display this value clearly inside your metrics table formatted to one decimal point (e.g., `f"{speedup:.1f}x"`).

---

### Constraints Checklist

* [ ] No utilization of synchronous blocking commands like `time.sleep()`. All waiting cycles must use non-blocking `await asyncio.sleep()`.
* [ ] Explicit use of static type annotations outlining all input parameters and expected primitive return values.
* [ ] The `TaskGroup` implementation must run safely alongside an `asyncio.Semaphore` constraint wrapper to accurately enforce the active worker pool maximum size.
* [ ] If the execution parameters define 20 tasks with a 300ms base and a 10-worker concurrent ceiling, your application table must show the TaskGroup batch completing in roughly two sequential flight cycles (~600ms total time).

```

---

### Why this works perfectly for Chapter 10:
* **The Monotonic Realization**: Forcing students to benchmark code using high-resolution timers highlights the precision required when auditing distributed systems and web software.
* **Semaphore Boundaries**: Seeing the `TaskGroup` take exactly twice as long as `gather` when the semaphore is restricted to half the total task count explicitly visualizes queue pooling and resource limits. It perfectly demonstrates the core compromise of architecture: **balancing maximum throughput versus system safety**.

```