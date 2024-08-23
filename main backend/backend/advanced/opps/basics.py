# class parant:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
#
# obj=parant("jiffin","55")

# class with function


# class Parant:
#     def __init__(self,name,age,dept):
#         self.name=name
#         self.age=age
#         self.dept=dept
#
#     def myfunction(self):
#         print("hello my name is",self.name,"im",self.age,self.dept)
#
# s1=Parant("abin","25","python")
# s2=Parant("diya","12","cs")
#
# s1.myfunction()
# s2.myfunction()
#
# s1.name="amar"
# print(s1.name)
#
# # del s1
# # print(s1.name)

# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def pri(self):
#         print("my name is",self.name,"im",self.age,"yr old boy")
#
# class teacher():
#     def __init__(self,join):
#         self.join=join
#
#     def pri2(self):
#         print("joined time",self.join)
#
# class EXstudent(Student,teacher):
#     def __init__(self,name,age,pass_out,join):
#         Student.__init__(self,name,age)
#         teacher.__init__(self,join)
#         self.pas_out=pass_out
#
#     def pri1(self):
#         print("my batch is",self.pas_out)
#
#
# obj=EXstudent("abin","24","2020","2017")
# obj.pri()
# obj.pri1()
# obj.pri2()


class cat():
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def pri(self):
        print("id",self.id,"name",self.name)

class brand():
    def __init__(self,br_id,br_name):
        self.br_id=br_id
        self.br_name=br_name

    def pri1(self):
        print("br id",self.br_id,"br name",self.br_name)

class model():
    def __init__(self,m_id,m_name,m_year):
        self.m_id=m_id
        self.m_name=m_name
        self.m_year=m_year

    def pri2(self):
        print("m id", self.m_id, "m name", self.m_name,"m year",self.m_year,)

class method(cat,brand,model):
    def __init__(self,prize,id,name,br_id,br_name,m_id,m_name,m_year):
        cat.__init__(self,id,name)
        brand.__init__(self,br_id,br_name)
        model.__init__(self,m_id,m_name,m_year)
        self.prize = prize

    def pri3(self):
        print("prize",self.prize)


obj=method("10","1","ain","2a","banana","12","jkl","2022")
obj.pri()
obj.pri1()
obj.pri2()
obj.pri3()


