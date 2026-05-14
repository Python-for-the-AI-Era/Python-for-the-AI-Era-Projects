# Project 08: Multi-Model Inventory System

### Overview
This project serves as a comprehensive capstone for modern backend database patterns. Production-grade software demands absolute safety under concurrent load. You will build a rock-solid, non-blocking asynchronous data infrastructure incorporating explicit ACID row locks inside `SQLAlchemy 2.0`, implement a highly performant Cache-Aside mechanism via `Redis`, handle structural system evolution tracking with `Alembic`, and integrate unstructured review graphs using `MongoDB` via `Motor`.

---

### The Architecture Contract

Your implementation must strictly satisfy these core data engineering rules:

#### 1. Atomic Concurrency Controls (`with_for_update`)
In high-velocity inventory management systems, two concurrent requests attempting to decrement stock simultaneously can cause an issue known as a **Race Condition**. 
* **The Rule**: Inside your `update_stock()` routine, you must execute your select queries using an explicit write lock statement:
  ```python
  stmt = select(Product).where(Product.id == product_id).with_for_update()

```

This instructs the underlying database engine (e.g., PostgreSQL) to append a `FOR UPDATE` modifier, locking that specific database row. Any subsequent network threads trying to modify the same element will wait safely in line until your overarching `session.begin()` transaction block terminates and issues a definitive database `COMMIT`.

#### 2. The Cache-Aside Read Pattern

To prevent redundant database access bottlenecks, all point lookups for single products must use an in-memory caching pattern:

* Always check the Redis key space `product:{id}` first.
* On a cache miss, route execution downward to query the core SQL tables, serialize the resulting SQLAlchemy object model into a standard JSON string, and store it in Redis using an explicit Time-To-Live (TTL) expiration set to `300` seconds (5 minutes).
* **Cache Invalidation**: Any operation that alters stock levels or updates a product's description must instantly remove the matching cache key to ensure data remains consistent.

#### 3. Database Schema Evolutions via Alembic

Database structures cannot be dropped and recreated from scratch in production. You must configure `Alembic` to track and generate system migrations step-by-step:

* **Migration 1**: Initial creation mapping your `Product`, `Category`, and `StockMovement` relational database tables.
* **Migration 2**: Alteration execution injecting the `reorder_level` integer column into the `Product` table with a safe schema migration fallback value defaulting natively to 10 (`server_default='10'`).
* You must verify structural capability by completing full cycle test passes: `alembic upgrade head` followed by `alembic downgrade -1`.

#### 4. The Data Check Constraint

To guarantee absolute physical system integrity, do not rely purely on Python application logic to protect against negative inventory counts. You must add a hard database-level Check Constraint directly inside your SQLAlchemy model definitions:

```python
__table_args__ = (
    CheckConstraint('stock_count >= 0', name='check_stock_non_negative'),
)

```

---

### Technical Signposts & Hints

#### 1. Formulating Multi-Table Aggregations

When constructing your outbound performance metric report, you need to combine tables and aggregate data. Join the `Product` table to the `StockMovement` table, filter out inbound entries by keeping only records where `quantity_delta < 0`, group the records by the product ID, and order the output by the sum of the movement deltas:

```python
# Conceptual SQLAlchemy expression outline
stmt = (
    select(Product.name, func.sum(StockMovement.quantity_delta).label("total_sold"))
    .join(StockMovement)
    .where(StockMovement.quantity_delta < 0)
    .group_by(Product.id)
    .order_by(func.sum(StockMovement.quantity_delta).asc()) # Ascending because deltas are negative
)

```

#### 2. Bonus Challenge: Polyglot MongoDB Synchronization

When pairing MongoDB review records alongside core relational PostgreSQL lines via the `Motor` client, remember that MongoDB uses a string or Object ID framework. Store the product's unique alphanumeric code (`product_sku`) as the indexing key across both systems. When calculating the average review rating using an aggregation pipeline, set a longer cache expiration threshold in Redis (e.g., 1 hour / 3600 seconds), as review stats are significantly less volatile than live inventory stock counts.

---

### Constraints Checklist

* [ ] No synchronous database drivers are permitted; you must use `asyncmy`, `asyncpg`, or equivalent asynchronous connection strings.
* [ ] Explicit use of session transactional context managers (`async with session.begin():`).
* [ ] Redis client actions must use the `redis.asyncio` protocol layer to avoid blocking the main event loop.
* [ ] All database model properties, query schemas, and transaction inputs must carry distinct PEP 484 type annotations.

```

---

### Why this works perfectly for Chapter 08:
* **Row-Level Locking (`with_for_update`)**: This introduces students to the realities of transactional systems, teaching them how database engines manage data conflicts under heavy real-world traffic.
* **Polyglot Database Management**: It breaks the habit of trying to force every piece of app data into a single database structure, showing them how to use Relational tables for transactions, NoSQL for text reviews, and Key-Value stores for ultra-fast caching.

```