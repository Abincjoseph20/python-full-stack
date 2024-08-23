# class father:
#     def setval(self,fname):
#         self.fname=fname
#     def prinval(self):
#         print("father name is",self.fname)
#
# class mother:
#     def setval1(self,mname):
#         self.mname=mname
#     def printval1(self):
#         print("mother name is",self.mname)
#
# class son(father,mother):
#     def setval2(self,sname):
#         self.sname=sname
#     def prinval2(self):
#         print("son name=",self.sname)
#
# obj=son()
# obj.setval("333")
# obj.setval1("222")
# obj.setval2("32 32 32")
# obj.prinval()
# obj.printval1()
# obj.prinval2()


# con
class company:
    def __init__(self,companyname,location):
        self.companyname=companyname
        self.location=location

class teamleader:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class worker(company,teamleader):
    def __init__(self,title,salary,companyname,location,name,id):
        company.__init__(self,companyname,location) #self koodi /object nde refference ahne self
        teamleader.__init__(self,name,id)

        self.title=title
        self.salary=salary

    def printval(self):
        print(self.companyname)
        print(self.location)
        print(self.name)
        print(self.id)
        print(self.title)
        print(self.salary)

obj=worker("dd","40000","gfc","kakkanad","hhh","1")
obj.printval()