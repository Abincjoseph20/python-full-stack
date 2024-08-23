# class parant:
#     def A1(self):
#         print("iam parant")
# class child(parant):
#     def b1(self,name):
#         print("iam child")
#         self.n=name
#
# obj=child()
# obj.b1("jiffin")
# obj.A1()
#
# obj1=child()
# obj1.b1("johny")




# class grandFather:
#     def setval(self,gname,address):
#         self.gname=gname
#         self.address=address
#
#     def printval(self):
#         print("my grand father is",self.gname)
#         print("our address is",self.address)
# class father(grandFather):
#     def setval1(self,fname,location):
#         self.fname=fname
#         self.location=location
#     def printval1(self):
#         print("im son of",self.fname)
#         print("im from",self.location)
#
# obj=father()
# obj.setval("d","c")
# obj.setval1("j","ktm")
# obj.printval()
# obj.printval1()



class father:

    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone

    def printval(self):
        print("father name",self.name)
        print("address",self.address)
        print("location",self.phone)


class son(father):
    def __init__(self,name,address,phone,son_name):
        super().__init__(name,address,phone) #thottu mukalile inint function ne call cheyyan use cheyyunna oru function ahne
        self.son_name=son_name

    def printval1(self):
        print("son's name=",self.son_name)

obj=son("a","ff","551","gfgfcf")
obj.printval()
obj.printval1()
