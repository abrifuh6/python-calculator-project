# Function to add numbers
def add(x, y):
    return x + y

# Function to subtract numbers
def subtract(x, y):
    return x - y 

# Function to multiply numbers
def multiply(x, y):
    return x * y

# Function to divide numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Welcome to Your Calculator")

# For spacing. 
print()

while True:
    print("Select Operation: \n (1) - Addition \n (2) - Subtraction \n (3) - Multiplication \n (4) - Division")
    operation = input("Enter your Choice (1/2/3/4 ?): ")
    print()
    # Using float to nest my input because it can take both integer and decimal numbers. 
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    if operation == "1":
        print("Answer is:", add(num1, num2))
    elif operation == "2":
        print("Answer is:", subtract(num1, num2))  
    elif operation == "3":
        print("Answer is:", multiply(num1, num2))  
    elif operation == "4":
        print("Answer is:", divide(num1, num2)) 
    else:
        print("Invalid operation") 
        
    print()
        
    print("---") 
