
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon,
# __iter__() and __next__() are used

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(myit)

print(next(myit))
print(next(myit))
print(next(myit))


# Do for Loops Have Iterators?
# Yes! For loops automatically use iterators under the hood.

# When you write a for loop, Python:
# Calls iter(iterable) to get an iterator object.
# Calls next(iterator) in each iteration.
# Stops when StopIteration is raised.

numbers = [1, 2, 3]

# What Python does internally in a for-loop:
iterator = iter(numbers)  # Step 1: Get an iterator
print(next(iterator))     # Step 2: Get next value → 1
print(next(iterator))     # Step 2: Get next value → 2
print(next(iterator))     # Step 2: Get next value → 3
print(next(iterator))     # Step 3: StopIteration error!

for num in numbers:
    print(num)  # Internally calls next()
