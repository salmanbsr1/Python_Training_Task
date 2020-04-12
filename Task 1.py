# Get two inputs from user
x = input("Enter first number: ")
y = input("Enter second number: ")

# divide x and y and store in z and print z
try:
    z = int(x)/int(y)
    print(z)

# Handle ZeroDivision Error is user input zero
except ZeroDivisionError as e:
    print("Error Code:",e)

# Handle ValueError if user input invalid value
except ValueError as ve:
    print("Error code: ",ve)