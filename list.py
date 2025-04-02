import random

arr=["Ayush", "bob", "Charlie", "Danny", "Eqbal"]

print(arr)
print(len(arr))
print(type(arr))
print(arr[-1])
print(arr[2])

# NOTE :
# notice all inbuilt datat types are mutable 
# Except Strings and Tuples which are Immmutable


# ------------------------------------------------------------------------
# LIST METHODS -> append(val), count(ele), pop(indx), remove(val), reverse(), sort(), insert(pos, val), index(val)

x = []
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.append(5)


print(x)
print(f"count of 5 is {x.count(5)}")
x.remove(5)
print("after removing 5 once :")
print(x)
x.pop(1)   #pops the 2nd element
print("after removing the elements at 2nd pos :")
print(x)

print("reversing the list : ")
x.reverse()
print(x)

print("randomizing the elements in x array :")
random.shuffle(x)
print(x)

print("sorting the array x :")
x.sort()
print(x)

print("now adding 2 at the second position :")
x.insert(1, 2)     # insert(pos, ele)
print(x)


# -----------------------------------------------------------------
# Unpacking of a list 
# IMP->requires same number of variables

l2=[1,2,3,4,5]
a,b,c,d,e=l2
print(a, b, c, d, e)