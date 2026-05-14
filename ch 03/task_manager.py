import sys
import copy
from datetime import datetime
from collections import defaultdict, deque
import heapq

# --- GLOBAL OR STATE STORAGE ---
# Students must manage these collections inside their functions
tasks_list = []                # Primary O(N) storage
priority_heap = []             # Min-heap or Max-heap storage for high priority tasks
tag_index = defaultdict(list)  # O(1) Reverse-index lookup by tag
undo_stack = deque(maxlen=10)  # Fixed-size history buffer

def save_state():
    """
    TODO: Push a deep copy of the current tasks_list onto the undo_stack
    before any modifying operation. Use copy.deepcopy().
    """
    pass

def add_task(title: str, priority: int, tags: set):
    """
    TODO: Create a task dictionary, append it to tasks_list, 
    push it to the priority_heap, and index it in tag_index.
    """
    save_state()
    pass

def complete_task(task_id: int):
    """
    TODO: Mark a task's status as 'done' inside tasks_list.
    Updates must reflect across indexes if applicable.
    """
    save_state()
    pass

def get_next():
    """
    TODO: Pop and return the highest priority pending task from priority_heap.
    """
    pass

def get_by_tag(tag: str) -> list:
    """
    TODO: O(1) lookup of tasks containing the given tag using tag_index.
    """
    pass

def undo():
    """
    TODO: Pop the last state from undo_stack and restore tasks_list.
    Rebuild auxiliary heaps/indexes to match restored state.
    """
    pass

def print_dashboard():
    """
    TODO: Process and format the active metrics to print the dashboard terminal UI.
    """
    pass

def main():
    # Example interactive loop or pre-loaded test sequences
    print("In-Memory Task Manager Initialized.")
    pass

if __name__ == "__main__":
    main()