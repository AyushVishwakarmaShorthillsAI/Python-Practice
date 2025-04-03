# for reducing if-else
# used for writing else if statement in one liner
n=5
res = 'Even' if n%2==0 else 'Odd' 
print(res)


# ternary operator in tuple 
# SYNTAX : (condition_is_false, condition_is_true)[condition]
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)  