

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {9, 10}

# Adding elements to a set
set1.add(6)
# set1 is now {1, 2, 3, 4, 5, 6}

# Removing elements from a set
set1.remove(6)
# set1 is now {1, 2, 3, 4, 5}

# Discarding elements from a set (no error if element not found)
set1.discard(5)
# set1 is now {1, 2, 3, 4}

# Popping an element from a set
popped_element = set1.pop()
# popped_element is 1 (or any other element, as sets are unordered)
# set1 is now {2, 3, 4}

# Clearing a set
set1.clear()
# set1 is now set()

# Union of sets
union_set = set2.union(set3)
# union_set is {4, 5, 6, 7, 8, 9, 10}

# Intersection of sets
intersection_set = set2.intersection(set3)
# intersection_set is set()

# Difference of sets
difference_set = set2.difference(set3)
# difference_set is {4, 5, 6, 7, 8}

# Symmetric difference of sets
symmetric_difference_set = set2.symmetric_difference(set3)
# symmetric_difference_set is {4, 5, 6, 7, 8, 9, 10}

# Checking subset
is_subset = set3.issubset(set2)
# is_subset is False

# Checking superset
is_superset = set2.issuperset(set3)
# is_superset is False

# Checking disjoint sets
is_disjoint = set2.isdisjoint(set3)
# is_disjoint is True

# Updating a set with another set
set2.update(set3)
# set2 is now {4, 5, 6, 7, 8, 9, 10}

# Updating a set with intersection
set2.intersection_update({6, 7, 8, 9})
# set2 is now {6, 7, 8, 9}

# Updating a set with difference
set2.difference_update({7, 8})
# set2 is now {6, 9}

# Updating a set with symmetric difference
set2.symmetric_difference_update({9, 10})
# set2 is now {6, 10}

# Looping through a set
for element in set2:
    print(element)
# Output: 6 10

# Set comprehension
set_comprehension = {x * 2 for x in range(5)}
# set_comprehension is {0, 2, 4, 6, 8}

# Frozen set (immutable set)
frozen_set = frozenset([1, 2, 3, 4, 5])
# frozen_set is frozenset({1, 2, 3, 4, 5})

# Union with frozen set
union_with_frozen = frozen_set.union({6, 7})
# union_with_frozen is frozenset({1, 2, 3, 4, 5, 6, 7})

# Intersection with frozen set
intersection_with_frozen = frozen_set.intersection({3, 4, 5, 6})
# intersection_with_frozen is frozenset({3, 4, 5})

# Difference with frozen set
difference_with_frozen = frozen_set.difference({4, 5})
# difference_with_frozen is frozenset({1, 2, 3})

# Symmetric difference with frozen set
symmetric_difference_with_frozen = frozen_set.symmetric_difference({4, 5, 6})
# symmetric_difference_with_frozen is frozenset({1, 2, 3, 6})

# Checking subset with frozen set
is_subset_frozen = frozen_set.issubset({1, 2, 3, 4, 5, 6})
# is_subset_frozen is True

# Checking superset with frozen set
is_superset_frozen = frozen_set.issuperset({1, 2})
# is_superset_frozen is True

# Checking disjoint with frozen set
is_disjoint_frozen = frozen_set.isdisjoint({6, 7})
# is_disjoint_frozen is True

# Creating a set from a list
set_from_list = set([1, 2, 3, 4, 5])
# set_from_list is {1, 2, 3, 4, 5}

# Creating a set from a string
set_from_string = set("hello")
# set_from_string is {'h', 'e', 'l', 'o'}

# Creating a set from a tuple
set_from_tuple = set((1, 2, 3, 4, 5))
# set_from_tuple is {1, 2, 3, 4, 5}

# Creating a set from a dictionary (keys only)
set_from_dict = set({"a": 1, "b": 2, "c": 3})
# set_from_dict is {'a', 'b', 'c'}

# Checking membership
is_member = 3 in set_from_list
# is_member is True

# Checking non-membership
is_not_member = 6 not in set_from_list
# is_not_member is True

# Copying a set
copied_set = set_from_list.copy()
# copied_set is {1, 2, 3, 4, 5}

# Length of a set
set_length = len(set_from_list)
# set_length is 5

# Minimum value in a set
min_value = min(set_from_list)
# min_value is 1

# Maximum value in a set
max_value = max(set_from_list)
# max_value is 5

# Sum of all elements in a set
sum_of_elements = sum(set_from_list)
# sum_of_elements is 15

# Checking if all elements are true
all_true = all({1, 2, 3})
# all_true is True

# Checking if any element is true
any_true = any({0, 1, 2})
# any_true is True

# Enumerating a set
enumerated_set = list(enumerate(set_from_list))
# enumerated_set is [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# Zipping sets
zipped_sets = list(zip(set_from_list, set_from_tuple))
# zipped_sets is [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

# Unzipping sets
unzipped_sets = list(zip(*zipped_sets))
# unzipped_sets is [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]