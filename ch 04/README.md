
# Project 04: Functional Data Pipeline

### Overview
This project challenges you to build a highly optimized, composable data pipeline using pure functional programming paradigms. Instead of using traditional loops or hardcoded class orchestration, you will utilize higher-order functions, closures for state isolation, decorators for runtime modification, and standard library functional utilities (`functools`).

You will process 10,000 strings through a sequence of modular transformations, monitoring execution speeds and cache metrics along the way.

---

### The Architecture Contract

Your implementation must expose the following core components:

#### 1. The `Pipeline` Class
Acts as the central orchestrator for your data transforms.
* `pipe(fn)`: Appends a transformation function to an internal registry. It must support **fluent method chaining** (e.g., `pipeline.pipe(f1).pipe(f2)`).
* `__call__(data)`: Transforms the class instance into a callable object, executing the registered transformations sequentially over the input list of strings.

#### 2. The Transformation Suite
Each function must accept a `List[str]` and return a modified `List[str]`.
* `clean_whitespace(strings)`: Strips leading/trailing spaces and internal duplicate spacing.
* `to_lowercase(strings)`: Converts all text to lowercase.
* `remove_duplicates(strings)`: Removes duplicate strings while preserving original sequence order.
* `filter_by_length(min_len)`: A **closure** that returns a function to filter out short strings.
* `capitalise_words(strings)`: Capitalizes the first letter of every word.
* `limit(n)`: A **closure** that returns a function capping the output array size to `n` elements.

---

### Technical Signposts & Hints

#### 1. Method Chaining via `return self`
To allow your readers to chain pipeline stages gracefully, the `.pipe()` method must modify its internal list of functions and then explicitly return `self`. This enables configuration syntax like:
```python
pipeline = Pipeline().pipe(clean_whitespace).pipe(to_lowercase)

```

#### 2. Metaclass Preservation with `@functools.wraps`

When writing your `@timer` and `@validate` decorators, remember that modifying functions at runtime natively destroys their metadata (like `__name__`).

* **Signpost**: Always use the `@functools.wraps(func)` decorator factory right above your inner execution wrapper function. Without this, your execution log will print the generic wrapper name instead of the true target stage (e.g., logging `wrapper` instead of `clean_whitespace`).

#### 3. Pipeline Composition via `functools.reduce`

The project requires you to take two independent `Pipeline` instances and fuse them together into a single pipeline sequence. Because a functional pipeline is essentially a reduction step—where the output of function $A$ becomes the input to function $B$—you can use `functools.reduce` to fold data down a sequence of callables:

```python
# Conceptual layout of functional reduction
final_data = functools.reduce(lambda accum, function: function(accum), list_of_functions, raw_data)

```

#### 4. Monitoring Cache Performance

You must decorate a standalone `normalise(string)` utility function using `@lru_cache`. At the very end of your program execution, you can inspect the performance metrics of this cache by querying its built-in metadata method:

```python
stats = normalise.cache_info()
print(f"Cache Hits: {stats.hits} | Misses: {stats.misses}")

```

---

### Constraints Checklist

* [ ] **Type Annotations**: All higher-order functions, callbacks, and closures must have distinct, complete PEP 484 type hints.
* [ ] **No State Spills**: Functions must not mutate global state variables. Closures must manage their target parameters (like `min_len` or `n`) purely through lexical scoping.
* [ ] **No Third-Party Tools**: Use only standard library modules (`time`, `functools`, `concurrent.futures`).
* [ ] **Validation Factory**: The `@validate` decorator must accept a callable predicate constraint dynamically, throwing a clean `ValueError` if the predicate evaluations fail.

```
