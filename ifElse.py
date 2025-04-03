# x=int(input("Please enter a number:"))
x=0

# if-elif-else statement

if x<0 :
    print("Negative Value")
elif x == 0:
    print("Zero Value")
else :
    print("Positive Value")

# ------------------------------------------------------------------------------------

# For statement -> for interating over individual elements of array, string, etc.

lst=[1,24, 7, 5, 34, 0, 12, 52]

for x in lst:
    print(f"{x}", end=" ")

# Range clause -> for iterating over a range, 
# Syntax -> range(start, end, steps) = start to end with step 'steps'

# for "New line" just use print()
print()

for i in range(5):
    print(i, end=" ")

print()
for i in range(23, 28):
    print(i, end=" ")

print()
for i in range(50, 60, 2):
    print(i, end=" ")

# array iteration using len
print("\nArray Iteration :")                #'\n' for new line Escape Sequenece
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])