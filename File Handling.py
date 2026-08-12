file = open("python.txt", "w")
file.write("I am learning Python")
file.close()

with open("python.txt", "r") as file:
    print(file.read())
