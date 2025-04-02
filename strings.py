
# String format => to insert some variable with string

name="Ayush"
Age=23
txt='my name is {}, age is {}'.format(name, Age)

print(txt)

# -----------------------------------------------------------
# Negative indexing in string

size=len(name)
print(name[-1])
print('str[-1] == str[(len-1)-1]')
print(name[size-1])

# Note that the strings are immutable in python
# name[0]='a'
# print(name)

# then how to change/manipulate strings ??

# ------------------------------------------------------------
# fstrings (similar to format)
# Syntax : str= f"hey, this side {name}, My age is {Age}"    ~  "hey, this side {}, My name is {}".format(name, Age)

print(f"Hey, this side {name}, My age is {Age}")