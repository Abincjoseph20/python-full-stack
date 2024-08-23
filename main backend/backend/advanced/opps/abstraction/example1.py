#
# from abc import ABC,abstractmethod
# class car(ABC): #abstact class is car
#     @abstractmethod # decorator // function structure ill differebce varathathe modify cheyyan.
#     def mileage(self):
#         pass
#
#     @abstractmethod
#     def wheels(self):
#         pass
#
#     def display(self):
#         pass
#
# class tesla(car):
#     def mileage(self):
#         print("milage is 30kmph")
#
#     def wheels(self):
#         print(" 4 wheels")
#
# class suzuki(car):
#     def mileage(self):
#         print("milage is 40kmph")
#
#     def wheels(self):
#         print("4 wheels")
#
# class  renault(car):
#     def mileage(self):
#         print("milage is 56kmph")
#
#     def wheels(self):
#         print("4 wheels")
#
# class dustor(car):
#     def mileage(self):
#         print("milage is 56kmph")
#
#     def wheels(self):
#         print("4 wheels")
#
# tes=tesla()
# tes.mileage()
# tes.wheels()
#
# reno=renault()
# reno.wheels()
# reno.mileage()
#
# suz=suzuki()
# suz.mileage()
#
# du=dustor()
# du.mileage()


# using constructor

from abc import ABC,abstractmethod

class exampleclass(ABC):
    @abstractmethod
    def __init__(self):
        pass

class subclass1(exampleclass):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("sum is:",a+b)

class subclass2(exampleclass):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("difference is:", a-b)

s1=subclass1(2,4)
s2=subclass2(10,100)