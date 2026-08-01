while True:

    num1 = int(input("Enter your first number: "))
    operator = input("Enter your operator: ")
    num2 = int(input("Enter your second number: "))


    if operator == "+":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)

    elif operator == "^":
        print(num1 ** num2)

    else:
        print("Invalid operator")


    answer = input("Continue? (yes/no): ").lower()
    if answer == "no":
        break

print("Goodbye, Thank you for using this program")