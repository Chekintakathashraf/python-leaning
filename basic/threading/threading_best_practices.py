# threading_best_practices.py
# Documentation: This file covers advanced topics, best practices, and handling exceptions in threading.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Module 9: Thread Priority - Simulating Thread Priorities

def priority_task(priority):
    """
    Simulate thread priority by printing the priority level.
    Thread priorities aren't directly supported, so we simulate it using time.sleep().
    """
    print(f"Thread with priority {priority} starting.")
    time.sleep(0.5)  # Simulate work
    print(f"Thread with priority {priority} finished.")

# Create and start threads with different priorities
threads = []
for priority in range(1, 4):  # Simulate priority levels
    t = threading.Thread(target=priority_task, args=(priority,))
    threads.append(t)

# Start threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Priority task simulation complete.")


# Module 10: Main Thread - Understanding the Role of the Main Thread

def main_thread_task():
    """Task function for the main thread to execute."""
    print("Main thread starting.")
    time.sleep(1)
    print("Main thread finished.")

# Create and start a thread
main_thread = threading.Thread(target=main_thread_task)
main_thread.start()

# Wait for the main thread to finish
main_thread.join()

print("Main thread has completed.")


# Module 11: Synchronization - Using Semaphore for Thread Coordination

semaphore = threading.Semaphore(2)  # Allow only 2 threads at a time

def semaphore_task():
    """Task that is controlled by a semaphore to limit concurrent access."""
    semaphore.acquire()
    try:
        print(f"Thread {threading.current_thread().name} is accessing the resource")
        time.sleep(2)
    finally:
        semaphore.release()

# Creating threads that will be controlled by the semaphore
threads = []
for _ in range(5):
    t = threading.Thread(target=semaphore_task)
    threads.append(t)

# Starting threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Semaphore task complete.")


# Module 12: Exception Handling in Threads - Handling Thread Failures

def faulty_task():
    """A task that will deliberately raise an exception to demonstrate error handling in threads."""
    print("Faulty task starting.")
    time.sleep(1)
    raise ValueError("An error occurred in the thread!")

def safe_task():
    """Task that handles exceptions safely."""
    try:
        faulty_task()
    except Exception as e:
        print(f"Handled exception: {e}")

# Creating and starting the thread with exception handling
t1 = threading.Thread(target=safe_task)
t1.start()
t1.join()

print("Thread with exception handling has finished.")

