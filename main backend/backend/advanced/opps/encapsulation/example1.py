# publica and private data type calling differnce

# class employe:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary #private data ahne so error
#
# emp1=employe("jose",10000)
# print(emp1.name)
# print(emp1.salary)


# using public function through callig private data members

# class employe:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary #private data ahne so error
#     def disp(self):
#         print("name:",self.name,"salary :",self.__salary)
#         self.salary1=self.__salary
#
# emp1=employe("jose",10000)
# emp1.disp()
#
# print(emp1.name)
# print(emp1.salary1)




# name angling
# class employe:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary #private data ahne so error
#     def disp(self):
#         print("name:",self.name,"salary :",self.__salary)
#         self.salary1=self.__salary
#
# emp1=employe("jose",10000)
# emp1.disp()
#
# print(emp1.name)
# print(emp1.salary1)
# print(emp1._employe__salary) #this is second method of calling private datas


