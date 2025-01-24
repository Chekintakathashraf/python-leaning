# threading_intro.py
# Documentation: This file covers the first 4 modules of Python threading
# from basic thread creation to understanding the thread lifecycle.

import threading
import time

# Module 1: Introduction to Threads - Simple Thread Creation and Joining

def simple_thread():
    """
    A simple thread function that simulates work by sleeping for 2 seconds.
    Demonstrates how to create and start a basic thread.
    """
    print("Thread is starting...")
    time.sleep(2)  # Simulate work by sleeping for 2 seconds
    print("Thread has finished.")

# Creating threads
threads = []
for _ in range(3):  # Create 3 threads
    t = threading.Thread(target=simple_thread)
    threads.append(t)

# Starting threads
for t in threads:
    t.start()

# Joining threads to ensure the main thread waits for them to finish
for t in threads:
    t.join()

print("All threads have completed.")


# Module 2: Thread Lifecycle - Understanding the States of a Thread

def thread_lifecycle():
    """
    This function demonstrates the basic thread lifecycle: 
    New -> Runnable -> Blocked -> Terminated.
    """
    print("Thread lifecycle demonstration started.")
    time.sleep(1)
    print("Thread lifecycle demonstration finished.")

# Create a single thread
t1 = threading.Thread(target=thread_lifecycle)
t1.start()  # Thread goes into Runnable state
t1.join()  # Wait for thread to finish (Terminated state)

print("Thread lifecycle example completed.")


# Module 3: Thread Creation and Starting

def print_message(message):
    """
    Simple thread function to print a message.
    Shows how to pass arguments to a thread function.
    """
    print(f"Message from thread: {message}")

# Create threads that accept arguments
threads = []
messages = ["Hello from Thread 1", "Hello from Thread 2", "Hello from Thread 3"]
for message in messages:
    t = threading.Thread(target=print_message, args=(message,))
    threads.append(t)

# Start threads
for t in threads:
    t.start()

# Join threads to ensure the main thread waits for completion
for t in threads:
    t.join()

print("All threads have printed their messages.")


# Module 4: Joining Threads - Ensuring Main Thread Waits for Sub-threads

def count_up_to(limit):
    """
    Function for a thread to count from 1 up to a given limit.
    Demonstrates using `join()` to wait for threads to complete.
    """
    for i in range(1, limit + 1):
        print(f"Counting: {i}")
        time.sleep(0.5)

# Create a thread to count up to 5
t1 = threading.Thread(target=count_up_to, args=(5,))
t1.start()

# Ensure main thread waits for t1 to complete
t1.join()

print("Counting thread has finished.")

