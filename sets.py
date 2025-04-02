# NOTE : normally can't create an empty set
# we need to use 'set()' constructor for doing this


# creating empty set -----------------------
st={}
print(type(st))

stK=set()             # empty set creation
print(type(stK))

# creating set with some elements --------------------
stN={1}
print(type(stN))

# sets are Unordered
# sets do Not Allow Duplicates
# Mutable
# set items can be of any datatype

# -------------------------------------------------------------
# set Methods -> add(ele), clear(), pop(val of ele), remove(val of element)

# maths methods of 2 or more sets -> union(), intersection(), difference(), etc

stK.add(1)
stK.add(2)
stK.add(3)
stK.add(4)

print(stK)

stK.pop()          # deletes a random element
print(stK)

stK.remove(3)
print(stK)

# what if element don't exist
# stK.remove(3)        # key error , since key not exist
# print(stK)

# set vs unordered set not here like in C++
# sets are unordered by default
# maps are ordered