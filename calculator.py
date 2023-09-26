from calculator_art import logo
from os import system

# Add func
def add(n1, n2):
    return n1 + n2

# Subtract func
def sub(n1, n2):
    return n1 - n2

# Multiply func
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    system("clear")
    print(logo)
    num1 = float(input("What is the first number?:"))
    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        operations_symbol = input("What is the operation?:")
        num2 = float(input("What is the second number?:"))
        answer = operations[operations_symbol](num1, num2)
        
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input("Type 'y' to use {answer} calculate or 'n' to create a new calculator:") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
            
if __name__ == '__main__':
    calculator()