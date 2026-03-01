try:
    int(input("enter you age:"))
except ValueError as ex:
    print("you have entered a wrong value",ex)