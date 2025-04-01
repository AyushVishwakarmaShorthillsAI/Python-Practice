import random


print('a random no. in a range b/w lower and higher value: ')
print(random.randrange(1, 10))

arr=[1,3,4,5,9,10,56,33, 88, 23, 11]
print('shuffles the array in a random order:')
random.shuffle(arr)
print(arr)

print('a random number b/w 0 and 1:')
print(random.random())