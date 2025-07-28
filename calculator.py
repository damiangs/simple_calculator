# Simple Calculator
# This is a simple calculator that can perform basic arithmetic operations
# such as addition, subtraction, multiplication, and division.

# sum function
def sum(a, b):
    return a + b

# subtract function
def subtract(a, b):
    return a - b

# multiply function
def multiply(a, b):
    return a * b

# divide function
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ask the user for input
def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

# main function to run the calculator
def main():
  print("Simple Calculator")
  print("Choose an operation:")
  print("1. Sum")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  # get user choice 
  choice = input("Enter choice (1/2/3/4): ")

  a, b = get_input()
  if choice == '1':
      print(f"The result is: {sum(a, b)}")
  elif choice == '2':
      print(f"The result is: {subtract(a, b)}")
  elif choice == '3':
      print(f"The result is: {multiply(a, b)}")
  elif choice == '4':
      try:
          print(f"The result is: {divide(a, b)}")
      except ValueError as e:
          print(e)
  else:
      print("Invalid choice")

  # check if the user wants to perform another calculation
  again = input("Do you want to perform another calculation? (yes/no): ")
  if again.lower() == 'yes':
      main()
  
  else:
      print("Thank you for using the calculator!")


if __name__ == "__main__":
    main()