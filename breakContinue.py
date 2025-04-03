
# The break statement breaks out of the "Innermost enclosing" for or while loop

for n in range(1, 10):
    print(f"iteration for : {n}")
    if n % 4 == 0:
        break

# nested loops
# break 
for i in range(1, 10):
    print(f'iteration for {i}')
    for x in range(1, i):
        print(x, end=" ")
        if x%5 == 0:
            break
    print()

# ---------------------------------------------------------------------------------------

#The continue statement continues with the next iteration of the loop
# continue

# printing only evens
print("printing only even with continue: ")
for n in range(1, 10):
    if n % 2 != 0:
        continue
    print(n, end=" * ")
    

print("\nprinting -------------------- ")

for i in range(1, 10):
    print(f'iteration for {i}')
    for x in range(1, i):
        if x%2 != 0:
            continue
        print(x, end=" ")
        
    print()

#-----------------------------------------------------------------------

# PASS statement
# pass statement does nothing. It acts as a placeholder for a function or conditional body .

# infinite waiting for input via keyboard

# while True:
#     pass      # use ctrl+C to bypass

#NOTE : after the 'pass' all the written code in VS code becomes dimmer indicating that something is left to be implemented


# def inintlog(*args):
#     pass            # remember to implement 

#---------------------------------------------------------------------------------------
