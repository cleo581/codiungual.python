class employee:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("destructor called")
def creatobject():
    print("creating objects")
    emp1=employee()
    return emp1

emp1=creatobject()
print("program ending")

        