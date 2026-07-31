def mohasebe(num1 , num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
       return num1 + num2

delbekhah1 = int(input("Enter a number: "))
delbekhah2 = int(input("Enter another number: "))
print(mohasebe(delbekhah1, delbekhah2))