num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

while True:
    operator = input("Enter operator such as '+', '-', '*', '/' : ")
    if operator == "+" or operator == "-" or operator == "*" or operator =="/":
        break
    else:
        print("You can only give input of '+', '-', '*', '/'")

if operator == '+':
    output = num1 + num2
elif operator == '-':
    output = num1 - num2
elif operator == '*':
    output = num1 * num2
elif operator == '/':
    while True:
        if num2 == 0:
            print("you cannot divide anything with 0.")
            num2 = int(input("Try another number : "))
        else:
            break
    output = num1 / num2

print(num1, operator, num2, "=", output)