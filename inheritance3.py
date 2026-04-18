class person(object):
    def __init__(self,name, idnum):
        self.name=name
        self.idnum=idnum
    def diplay(self):
        print("name:",self.name)
        print("idnum:",self.idnum)

class employee(person):
    def __init__(self,name,idnum,salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name,idnum)

ob1=employee("tommy", 123, 50000, "manager")
ob1.diplay()