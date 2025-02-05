def pre_increment(x):
    x += 1  # First increment
    return x  # Then return the new value

def post_increment(x):
    old_value = x  # Store current value
    x += 1  # Then increment
    return old_value  # Return original value

def pre_decrement(x):
    x -= 1  # First decrement
    return x  # Then return the new value

def post_decrement(x):
    old_value = x  # Store current value
    x -= 1  # Then decrement
    return old_value  # Return original value

if __name__ == "__main__":
    a = 5
    
    # Pre-Increment
    a = pre_increment(a)
    print("After Pre-Increment:", a)  # Output: 6
    
    # Post-Increment
    b = post_increment(a)
    print("After Post-Increment:", b, a)  # Output: 6 7
    
    # Pre-Decrement
    a = pre_decrement(a)
    print("After Pre-Decrement:", a)  # Output: 6
    
    # Post-Decrement
    b = post_decrement(a)
    print("After Post-Decrement:", b, a)  # Output: 6 5
