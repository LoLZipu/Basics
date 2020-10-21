def greeting(name,age=25):
    print(f"Hello Fellow VSC User {name}, you are {age}")

name = input("Enter your name: ")
age = input("Enter your age: ")
greeting(name,age)
greeting("Parth",22)