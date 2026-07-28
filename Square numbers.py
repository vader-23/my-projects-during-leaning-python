# the first way:
def square(x):
    result = 0

    if x >= 0:
        for i in range(x):
            result += x
    else:
        for i in range(-x):
            result += -x

    return result

num1 = int(input("enter your number: "))
print(square(num1))


# the second way:
def square(x):
    return x ** 2

num1 = int(input("enter your number: "))
print(square(num1))


# the third way:
def square(x):
    result = 0

    for i in range(x):
        result += x

    return result

num1 = int(input("enter your number: "))
print(square(num1))