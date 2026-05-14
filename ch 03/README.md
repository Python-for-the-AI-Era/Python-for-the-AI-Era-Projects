# Project 03: In-Memory Task Manager

### Overview
This project challenges you to design a compound data system. Instead of using a database, you will combine Python’s powerful native collections (`list`, `dict`, `set`, `defaultdict`, `deque`, and `heapq`) to manage data efficiently based on computational complexity constraints.

### Technical Signposts & Friction Points

1. **The Heap Priority Gotcha (`heapq`)**
   Python’s `heapq` module implements a *min-heap* by default (the smallest number sits at the top). Your project requires higher integers (5 down to 1) to be served first.
   - **Masterclass Strategy**: Invert your priority values when pushing onto the heap to turn it into a max-heap. For example, a priority of `5` becomes `-5`.
   - **Tuple Sorting**: Push tuples into the heap: `(negative_priority, task_id, task_dict)`. Python sorts tuples element-by-element. Including `task_id` ensures unique elements if priorities match.

2. **State Mutation & `copy.deepcopy()`**
   If you push `tasks_list` onto your `undo_stack` directly via `undo_stack.append(tasks_list)`, you are storing a reference to the exact same list. Modifying a task later will mutate the history stack too!
   - Always take an absolute independent snapshot using:
     ```python
     import copy
     undo_stack.append(copy.deepcopy(tasks_list))
     ```

3. **O(1) Tag Lookup with `defaultdict`**
   Searching for a tag across a massive raw list of tasks takes $O(N)$ time. To make lookup instantaneous ($O(1)$), update your index whenever a task is added:
   ```python
   for tag in tags:
       tag_index[tag].append(task)

```

4. **Tracking History with `deque**`
By defining a `deque(maxlen=10)`, Python handles buffer boundaries automatically. If an 11th operation occurs, the oldest history item is silently dropped from the left side, keeping memory usage bounded.

### Bonus Challenge: Task Dependencies via Sets

To check if a task is ready to be executed, find out if all its prerequisite task IDs exist within the set of fully completed task IDs. This can be checked instantly using set subsets or intersections:

```python
if prerequisites.issubset(completed_task_ids):
    # This task is unblocked!

```

### Constraints Checklist

* [ ] No third-party state engines or storage frameworks.
* [ ] Heap sorting must happen concurrently alongside array manipulation.
* [ ] Task search queries must utilize clear list comprehensions.
* [ ] The undo history buffer must never exceed 10 items.

```

---

### Why this is effective for Chapter 03:
* **The Heap Inversion Hack**: Forcing them to figure out that `-5` is smaller than `-1` to simulate a max-heap is a classic, essential low-level systems programming paradigm.
* **Deep Copying Habits**: It highlights the fundamental difference between memory addresses/references and actual standalone values, prepping them for advanced OOP and custom memory tracking concepts later.

```