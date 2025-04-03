# Match statement 
# takes an expression and compares its value to successive patterns given as one or more case blocks.

def httpStatusCodes(code):
    match code:
        case '1xx': 
            return "Information pass"
        case '2xx':
            return "Success"
        case '3xx':
            return "Redirection"
        case '4xx':
            return "Client Side Error "
        case '5xx':
            return "Server Side Error"

print(f"the status code 5xx refers to : {httpStatusCodes('5xx')}")

x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))

# Note : No pair like in C++, use tuples instead for the same
point=(x,y)

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
#Note : for default case, use '_'