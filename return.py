# to return multiple values use "Commas"
# return statement is optional
# the returned value can be can be any python object(INT, FLOAT, STRING, TUPLE, LIST, DICT, SET, CLASSES, FUNCTIONS, MODULES/PACKAGES)



# EXPLICIT RETURN :using return keyword, it immediately terminates a function executionr
# Ef : return 0 in a function

def f2():
    return 3

print(f2())

# ----------------------------------------------------------------------------------------------------------
# IMPLICIT RETURN : if no return statement, then python send "NONE" as the returned value

x=1
def f():
    print("HELLOOO (:)")
    
print(f())        # return NONE

# ------------------------------------------------------------------------------------------------------

# Returning Multiple Values
def f3():
    return 1,2,3,4,5,6

print(f3())       # returns a python tuple if Multiple values are returned

#-----------------------------------------------------------------------------------------------
# Can also return True or False
def Even(x):
    if x%2==0:
        return True
    else:
        return False

print(Even(6))

# ------------------------------------------------------------------------------------------------------
# return can be used for Short-Circuiting also
# after return stateement the below code is All Dead

# using return in try catch def func(value):
def func(value):
    try:
        return float(value)
    except ValueError:
        return str(value)
    finally:
        print("Run this before returning")

print(func("one"))
print(func(9))