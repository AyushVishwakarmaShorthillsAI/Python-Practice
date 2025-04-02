# () for tuples

t=()
print(type(t))

# Immutable and Ordered
# Allow duplicates

t=('a', 'b', 'c', 'a')
print(t)

# can't add or delete anything from a tuple 
# but can reassign variable

# -----------------------------------------
# Methods --> count(ele), index(ele)

print(f"the count of a is : {t.count('a')}")

print(f"the index of b is {t.index('b')}")