def add(a,b):
    return a+b
 
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("select a option")
print("a for addition")
print("b for subtraction")
print("c for multlipication")
print("d for division")

choice=input("please enter your choice")

num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
 
if choice=="a":
    print(add(num1,num2))
    
elif choice=="b":
    print(sub(num1,num2))

elif choice=="c":
    print(mul(num1,num2))

elif choice=="d":
    print(div(num1,num2))

else:
    print("invalid input")




   




