# enumerate() function adds a counter to each item in a list or other iterable.

a = ["Me", "I", "Myself"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
# can directly give numbering to elements and store in a list using enumerate
print(list(enumerate(a)))

print("I, I am, I am ~~~~~")