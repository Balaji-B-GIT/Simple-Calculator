from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  condition = True
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  while condition:
    choice = input(f"type 'Y' to continue with {first_answer} or type 'N' to start new calculation: ").lower()
    if choice == "y":
      operation_symbol = input("Pick another operation: ") 
      num3 = int(input("What's the next number?: "))
      calculation_function = operations[operation_symbol] 
      second_answer = calculation_function(first_answer, num3)
      print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
      first_answer = second_answer
    else:
      calculator()

calculator()