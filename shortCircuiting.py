# Short-circuiting makes Python faster by avoiding unnecessary evaluations.
# it can be used with and, or operators

# -----------------------------------------------------------------
# bypassing division by zero error using AND short circuiting

a = 0
b = 10
if a != 0 and (b / a > 5):  # Division by zero never happens!
    print("Valid")
else:
    print("Invalid")  # Output: Invalid


# ----------------------------------------------------------------------
# OR shortcircuiting

username = input("Enter username: ") or "Guest"
print("Hello,", username)



# ------------------------------------------------------------------
# ==  VS  is  operator in python

#   ==  ->  is for comparing values
#   is  ->  is for comparing the object they contain reference the variables are pointing to 
x = [1, 2, 3]
y = [1, 2, 3]
z = x


if x is y:
    print("True")
else:
    print("False")

if x is z:
    print("True")
else:
    print("False")