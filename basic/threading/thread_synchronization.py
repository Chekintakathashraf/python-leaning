# thread_synchronization.py
# Documentation: This file covers synchronization concepts such as Locks, RLocks, and Thread Pools.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Module 5: Synchronization - Using Locks

# Shared resource
counter = 0
lock = threading.Lock()

def increment_task():
    """
    Task that increments the counter safely using a lock.
    Demonstrates how to prevent race conditions with locks.
    """
    global counter
    with lock:  # Acquire the lock before modifying shared resource
        counter += 1
        print(f"Counter: {counter}")
    time.sleep(1)

# Creating threads that increment the counter
threads = []
for _ in range(5):
    t = threading.Thread(target=increment_task)
    threads.append(t)

# Starting threads
for t in threads:
    t.start()

# Joining threads to ensure the main thread waits for them to finish
for t in threads:
    t.join()

print(f"Final counter value: {counter}")


# Module 6: Using RLocks (Reentrant Locks)

def recursive_increment(n):
    """
    Function to increment a counter in a recursive way.
    Demonstrates using an RLock to allow reentrant locking by the same thread.
    """
    global counter
    if n > 0:
        rlock.acquire()  # Acquire the lock
        try:
            counter += 1
            print(f"Counter: {counter}")
            recursive_increment(n - 1)  # Recursively increment counter
        finally:
            rlock.release()  # Release the lock

# Creating an RLock (Reentrant Lock)
rlock = threading.RLock()

# Create and start the thread
t1 = threading.Thread(target=recursive_increment, args=(3,))
t1.start()
t1.join()

print(f"Final counter value after recursion: {counter}")


# Module 7: Thread Pooling - Managing Multiple Threads with ThreadPoolExecutor

def task():
    """Simple task function that simulates work."""
    print("Executing task...")
    time.sleep(1)

def main():
    """Main function that demonstrates using ThreadPoolExecutor to manage thread pools."""
    with ThreadPoolExecutor(max_workers=3) as executor:
        for _ in range(5):
            executor.submit(task)  # Submit tasks to the thread pool
    print("All tasks completed.")

# Run the main function
if __name__ == "__main__":
    main()


# Module 8: Daemon Threads - Threads that Run in the Background

def daemon_task():
    """
    Demonstrates a daemon thread that runs in the background.
    Daemon threads are automatically killed when the program exits.
    """
    print("Daemon thread started.")
    time.sleep(3)
    print("Daemon thread finished.")

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task, daemon=True)
daemon_thread.start()

# Main thread waits for a short time but exits before daemon thread finishes
time.sleep(1)
print("Main program exiting.")
