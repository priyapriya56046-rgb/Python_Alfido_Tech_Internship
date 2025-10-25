#Basic Calculator
import operator

# Dictionary of operations
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

print("Welcome to Enhanced Calculator!")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /) or 'exit' to quit: ").lower()
        
        if op == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if op in operations:
            if op == '/' and num2 == 0:
                print("Error: Division by zero")
            else:
                result = operations[op](num1, num2)
                print(f"{num1} {op} {num2} = {result}")
        else:
            print("Invalid operation! Please choose +, -, *, /")
    
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    
    print("-" * 30)  # separator for readability
