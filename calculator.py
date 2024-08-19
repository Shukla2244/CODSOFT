# COMMAND LINE APPLICATION OF CALCULATOR
# You can perform any arithmetic operation (add, subtract, multiply, divide, remainder, floor division, power).
# Exceptions are handled appropriately.

def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***CALCULATOR APP***\n")
    
    operations = {
        1: ("Addition", add),
        2: ("Subtraction", sub),
        3: ("Multiplication", mul),
        4: ("Division", div),
        5: ("Modulus", mod),
        6: ("Floor Division", flr),
        7: ("Power", power)
    }

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("8. EXIT")
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 8:
                print("\nExiting from Calculator......\n")
                break

            if choice not in operations:
                print("\nINVALID CHOICE, PLEASE TRY AGAIN\n")
                continue

            a = float(input("\nEnter the first number: "))
            b = float(input("Enter the second number: "))

            operation_name, operation_func = operations[choice]
            operation_func(a, b)

        except ValueError:
            print("\nINVALID INPUT, PLEASE ENTER NUMBERS ONLY\n")

def add(n, m):
    print(f"\nAddition of {n} and {m} is: {n + m}")
    print("________________________________________")

def sub(n, m):
    print(f"\nSubtraction of {n} and {m} is: {n - m}")
    print("________________________________________")

def mul(n, m):
    print(f"\nMultiplication of {n} and {m} is: {n * m}")
    print("________________________________________")

def div(n, m):
    if m == 0:
        print("\nCan't divide by zero")
    else:
        print(f"\nDivision of {n} and {m} is: {n / m}")
    print("________________________________________")

def mod(n, m):
    if m == 0:
        print("\nCan't divide by zero")
    else:
        print(f"\nModulus of {n} and {m} is: {n % m}")
    print("________________________________________")

def flr(n, m):
    if m == 0:
        print("\nCan't divide by zero")
    else:
        print(f"\nFloor division of {n} and {m} is: {n // m}")
    print("________________________________________")

def power(n, m):
    print(f"\n{n} to the power of {m} is: {n ** m}")
    print("________________________________________")

if __name__ == "__main__":
    main()
    print("\n\t\tThanks for using..........\n")
