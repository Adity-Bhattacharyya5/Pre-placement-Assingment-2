# Create dynamic array
arr = []

# Insertion
arr.append(10)          # Insert at end
arr.insert(0, 5)        # Insert at index 0
print("After insertions:", arr)

# Deletion
arr.pop()               # Remove last element
arr.pop(0)              # Remove element at index 0
print("After deletions:", arr)

# Search
arr = [1, 2, 3, 4, 5]
if 3 in arr:
    print("3 found at index", arr.index(3))

# Traversal
for val in arr:
    print(val, end=" ")

# Update
arr[2] = 99
print("\nAfter update:", arr)
