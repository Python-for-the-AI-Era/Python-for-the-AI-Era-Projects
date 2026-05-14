import asyncio
import time
import random
import argparse
from typing import List, Tuple

# --- SIMULATION TARGET ---

async def simulate_work(task_id: int, base_duration_ms: float, jitter_ms: float) -> float:
    """
    TODO: 
    1. Calculate a random sleep duration: base_duration_ms +/- a random uniform jitter value.
    2. Convert the millisecond value to seconds and call await asyncio.sleep().
    3. Return the exact time spent sleeping.
    """
    pass

async def run_worker_with_semaphore(sem: asyncio.Semaphore, task_id: int, base_dur: float, jitter: float) -> float:
    """
    TODO: Wrap the simulate_work routine inside an 'async with sem:' context block 
    to enforce a strict upper boundary on concurrent execution.
    """
    pass


# --- EXECUTION STRATEGIES ---

async def run_serial(num_tasks: int, base_dur: float, jitter: float) -> float:
    """
    TODO: Execute tasks completely sequentially using a standard for loop.
    Await each task explicitly before moving to the next. Measure and return total elapsed time.
    """
    pass

async def run_gather(num_tasks: int, base_dur: float, jitter: float) -> float:
    """
    TODO: Spawn all tasks simultaneously and pass them unpacked into asyncio.gather(*tasks).
    Measure and return total elapsed wall-clock time.
    """
    pass

async def run_task_group(num_tasks: int, base_dur: float, jitter: float, max_concurrent: int) -> float:
    """
    TODO: Use the modern 'async with asyncio.TaskGroup() as tg:' context manager.
    Combine this with an asyncio.Semaphore(max_concurrent) to spawn all tasks concurrently 
    while restricting the max active worker pool size.
    """
    pass


# --- MAIN ORCHESTRATION ---

async def main():
    parser = argparse.ArgumentParser(description="Async Concurrency Visualiser")
    parser.add_argument("--tasks", type=int, default=20, help="Number of simulated tasks")
    parser.add_argument("--duration", type=float, default=300, help="Base task duration in milliseconds")
    parser.add_argument("--jitter", type=float, default=50, help="Random uniform jitter range in milliseconds")
    parser.add_argument("--max-concurrent", type=int, default=10, help="Semaphore upper concurrency ceiling")
    
    args = parser.parse_args()
    
    print(f"\nRunning {args.tasks} tasks ({args.duration}ms ± {args.jitter}ms each)...")
    print("═" * 50)
    
    # 1. Execute and time Serial strategy
    # 2. Execute and time Gather strategy
    # 3. Execute and time TaskGroup strategy
    # 4. Calculate and output speedup ratios: (Serial Time / Concurrent Time)
    pass

if __name__ == "__main__":
    asyncio.run(main())