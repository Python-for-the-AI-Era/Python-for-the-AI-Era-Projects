# Project 11: Data Playground CLI

### Overview
This project targets structural data engineering and metacoding patterns. True data professionals do not blindly memorize frameworks; they evaluate processing performance profiles objectively. You will engineer an analytical terminal utility using the **Strategy Software Design Pattern** to seamlessly switch engine contexts between traditional **Pandas** (Row-major, Eager execution) and modern **Polars** (Columnar Arrow format, Lazy optimization query plans).

A critical requirement of this project is **Code Telemetry**: your tool must track its internal commands, printing the exact equivalent code execution strings alongside its terminal table readouts.

---

### The Architecture Contract

Your implementation must strictly satisfy these core data pipelining requirements:

#### 1. Eager vs. Lazy Execution Architecture
Your software must respect the core philosophy of each backend:
* **Pandas**: Run actions immediately upon object reference invocation via its traditional, in-memory single-threaded runtime.
* **Polars**: Prevent premature data processing overhead. You must load your file footprint context lazily via `pl.scan_csv()`. Build a deferred expression graph for summaries, aggregations, and evaluations, calling your structural optimizer explicitly at the last possible block using `.collect()`.

#### 2. Anomaly Highlighting Matrix
When computing the pairwise Pearson product-moment correlation matrix over numerical features (`df.corr()` or `df.select(pl.selectors.numeric()).corr()`), your CLI printer must inspect every element. If a feature covariance evaluation exceeds an absolute threshold metric of $> 0.7$, flag the relationship by applying raw terminal **ANSI color escape codes** directly inside your standard string outputs to highlight the strong link:
```python
# Print strong correlation elements using ANSI bold yellow highlights
print(f"\033[1;33m{feature_a} <-> {feature_b}: {coefficient:.2f}\033[0m")

```

#### 3. Interactive Code Telemetry Generation

When executing dynamic user-defined grouping requests, your program must act as an automated code generator. Capture the targeted variables (`group_by_col`, `agg_col`) using standard interactive Python `input()` buffers, execute the mathematical transform safely, and return a multi-line formatted code block showing the exact, valid syntax used:

```text
# Expected Polars Code Telemetry Output String:
lf.group_by('city').agg([
    pl.col('revenue').sum().alias('total'),
]).collect()

```

#### 4. Time-Series Sparklines

If the script detects a column containing datetime records, resample the timeline to a strict **Daily (`D`)** cadence, calculate total cumulative volumes, and print an ASCII sparkline graph charting the trend in the terminal:

* Construct the mini terminal graph using standard unicode block variations: ` ▂▃▄▅▆▇█`

---

### Technical Signposts & Hints

#### 1. Decoupling Logic via the Strategy Pattern

Do not write messy `if engine == 'pandas':` logical splits inside your main file workflows. This architecture quickly becomes unmaintainable. Instead, isolate your pipeline calls completely inside independent classes that inherit from the abstract `DataEngine` template. This decouples the operational runtime from the internal framework syntax.

#### 2. Building a Custom Percentile Mapping Matrix

Since Polars calculates quantile statistics using lazy, multi-threaded columnar aggregations and Pandas operates over numpy arrays, map your summary distributions consistently to a clean output schema dictionary matching this spec:

```python
summary_metrics = {
    "null_pct": null_count / total_rows * 100,
    "p25": calculated_quantile_0_25,
    "p50": calculated_median,
    "p75": calculated_quantile_0_75
}

```

---

### Constraints Checklist

* [ ] No cross-contamination of classes: Pandas modules must never import `polars`, and Polars engines must not fallback on `pandas` object conversions.
* [ ] All output string metrics must be cleanly rounded and formatted to a maximum limit of two decimal points.
* [ ] The CLI must run safely without crashing if a column contains structural `Null` or `NaN` missing records; calculate the exact missing entry percentages and list them clearly inside the summary table.
* [ ] Every concrete data method, abstract interface boundary, and formatting utility helper must include explicit PEP 484 static type hints.

```

---

### Why this works perfectly for Chapter 11:
* **The Telemetry Generation Mindset**: Forcing students to print the exact code string used to generate a data table shifts their thinking from writing single-use scripts to building **developer tooling and automated analytics platforms**.
* **Eager vs. Lazy Internalization**: By mapping the same functional requirement to both libraries simultaneously, students understand why Polars achieves massive performance gains over legacy toolsets. They learn that optimization isn't just about faster loops—it's about building and executing a structured **Logical Query Plan**.

```