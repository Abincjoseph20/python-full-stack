# class a:
#     def a1(self):
#         print("class a")
#
# class b(a):
#     def b1(self):
#         print("classs b")
#
# class c(a):
#     def c1(self):
#         print("class c")
#
#
# obj=b()
# obj1=c()
#
# obj.b1()
# obj.a1()
# obj1.c1()
#
#
#
# class details:
#     def setval(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#     def showdate(self):
#         print("\n","id:",self.id,"\n","name",self.name,"\n","gender",self.gender)
#
#
# class developer(details):
#     def setval1(self,company,department):
#         self.company=company
#         self.department=department
#
#     def showdate1(self):
#         print("company:",self.company,"\n","department:","\n",self.department)
#
#
# class doctor(details):
#     def setval2(self,hospital,specialize):
#         self.hospital=hospital
#         self.specialize=specialize
#
#     def showdate2(self):
#         print("hospital:",self.hospital,"\n","specialize:",self.specialize)
#
# obj=developer()
# obj1=doctor()
#
# obj.setval(120,"a","m")
# obj.showdate()
#
# obj.setval1("fff","non")
# obj.showdate1()
#
# obj1.setval(123,"b","m")
# obj1.showdate()
#
# obj1.setval2("take care","cardiology")
# obj1.showdate2()




# class details:

#     def __init__(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#
# class developer(details):
#     def __init__(self,company,department):
#         self.company=company
#         self.department=department
#
# class doctor(details):
#     def __init__(self,hospital,specialize):
#         self.hospital=hospital
#         self.specialize=specialize
#
#
#     def showdate2(self):
#         print(self.id)
#         print(self.name)
#         print(self.gender)
#         print(self.company)
#         print(self.department)
#         print(self.hospital)
#         print(self.specialize)
#
# obj=developer("hbh","it",)
# obj1=doctor("hbkhb","bbblhb",)
# obj1.showdate2()


# constructor
class details:
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
    def showdate(self):
        print("\n","id:",self.id,"\n","name",self.name,"\n","gender",self.gender)


class developer(details):
    def __init__(self,company,department,id,name,gender):
        self.company=company
        self.department=department
        details.__init__(self,id,name,gender)

    def showdate1(self):
        print("company:",self.company,"\n","department:","\n",self.department)


class doctor(details):
    def __init__(self,hospital,specialize,id,name,gender):
        self.hospital=hospital
        self.specialize=specialize
        details.__init__(self,id,name,gender)

    def showdate2(self):
        print("hospital:",self.hospital,"\n","specialize:",self.specialize)

obj=developer("bhh","vhjvh","hjkh","ggvkh","hkhkb")
obj1=doctor("vgvg","hjhbk","gvg","chg","v jgh")

obj.showdate()
obj.showdate1()

obj1.showdate()
obj1.showdate2()