from functions import operations
from art import logo

print(logo)
def calculator():
  end = False
  num1 = float(input("What's the first number?: "))
  for key in operations.keys():
    print(key)
  while not end:
    operation_symbol = input('Pick an operation: ')
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    cmd = input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation, or any keyword to exit: ").lower()
    if cmd == 'y':
      num1 = answer
    elif cmd == 'n':
      calculator()
    else:
      end = True

calculator()
