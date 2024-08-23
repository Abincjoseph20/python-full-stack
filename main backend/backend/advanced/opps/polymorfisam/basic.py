# a=5
#
# b=6
# c=7
# a=9
# print(a)
# def add(a,b):
#     print(a+b)
#
# def add(a,b,c):
#     print(a+b+c)
#
#
# add(a,b,c)
# add(a,b)


# method over riding

# class A:
#     def display(self):
#         print("class a")
#
# class B(A):
#     def display(self):
#         print("class b")
#
# obj=B()
# obj.display()


#
# class A:
#     def display(self):
#         print("class a")
#
# class B(A):
#     def display(self):
#         print("class b")
#         A.display(self) #parant class le function ne child class ill acess cheyyan //"self ahne evde argument"//
#
# obj=B()
# obj.display()

class parant1:
    def a1(self):
        print("first super class")
class parant2:
    def a1(self):
        print("secound parant class")
class child(parant2,parant1):
    def a1(self):
        print("from child")
        super().a1()
        parant1.a1(self)

obj=child()
obj.a1()