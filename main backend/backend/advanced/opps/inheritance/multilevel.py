# class parant1:
#     def a1(self):
#         print("first super class")
# class mediator(parant1):
#     def a2(self):
#         print("secound parant class")
# class child(mediator):
#     def a3(self):
#         print("child class")
#
# obj=child()
# obj.a1()
# obj.a2()
# obj.a3()
# print()


# class grandfather:
#     def setval(self,gname,address):
#         self.gname=gname
#         self.address=address
#     def printval(self):
#         print("my grand father is",self.gname)
#         print("our address is",self.address)
#
# class father(grandfather):
#     def setval1(self,fname,location):
#         self.fname=fname
#         self.location=location
#     def printval1(self):
#         print("im son of",self.fname)
#         print("im from",self.location)
#
# class child(father):
#     def setval2(self,name,job):
#         self.name=name
#         self.job=job
#     def printval2(self):
#         print("im",self.name)
#         print("my proffession is",self.job)
#
# obj=child()
# obj.setval("david","chenakalayil")
# obj.setval1("joseph","ktm")
# obj.setval2("abin","non")
#
# obj.printval()
# obj.printval1()
# obj.printval2()

# through constructor

class mobile:
    def __init__(self,storage,color):
        self.storage=storage
        self.color=color
    def printval(self):
        print("storage=",self.storage)
        print("color=",self.color)

class samsung(mobile):
    def __init__(self,storage,color,name):
        self.name=name
        mobile.__init__(self,storage,color)
    def printval1(self):
        print("name=",self.name)

class galaxi(samsung):
    def __init__(self,year,speed,name,storage,color):
        self.year=year
        self.speed=speed
        samsung.__init__(self,storage,color,name)
    def printval2(self):
        print("year=",self.year)
        print("speed=",self.speed)

obj=galaxi(storage="32gb",name="samsung",color="black",year="2009",speed="100")
obj.printval()
obj.printval1()
obj.printval2()