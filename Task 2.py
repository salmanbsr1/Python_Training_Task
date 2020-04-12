#Get an input from user
x = input("Enter your number: ")

#Print positive numbers, one corresponding to each .
try:
    if int(x) >=0:
        for l in range(int(x)):
            z = l*l
            print(z)

# Handle ValueError if user input invalid value
except ValueError as ve:
    print("Error code: ",ve)

#Returns negative value input message
else:
    print("Number you entered is negative value")