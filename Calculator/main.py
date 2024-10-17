import json
import os


def load_history(filename='history.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def save_history(history, filename='history.json'):
    with open(filename, 'w') as file:
        json.dump(history, file)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    
   
    history = load_history()
    
    while True:
        print("\nPrevious Calculations:")
        for i, calc in enumerate(history[-7:], 1):  
            print(f"{i}. {calc}")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
            print(operation)
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
            print(operation)
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
            print(operation)
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"
            print(operation)
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice! Please select a valid operation.")
            continue
        
        
        history.append(operation)
        save_history(history) 

if __name__ == "__main__":
    main()
