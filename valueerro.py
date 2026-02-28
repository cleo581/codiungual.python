try:
    number=int(input("enter a number"))
    print("the number is :",number)
except ValueError as ex:
    print("you have entered a wrong value",ex)
    

    


