# class a:
#     def a1(self):
#         print("class")
#
# class b(a):
#     def b1(self):
#         print("class b")
# class c(a):
#     def c1(self):
#         print("class c")
# class d(b,c):
#     def d1(self):
#         print("class d")
#
# obj=d()
#
# obj.a1()
# obj.b1()
# obj.c1()
# obj.d1()


# using constructor
#
# class univercity():
#     def __init__(self,univ_name):
#         self.univ_name=univ_name
#
#     def pri(self):
#         print("name of univercity=",self.univ_name)
#         print(f"name of univercity= {self.univ_name}") #evde {f} ennaththe koduthillangil worka villa erthe python format ane
#
#
#
# class course(univercity):
#     def __init__(self,univ_name,course_name):
#         univercity.__init__(self,univ_name)
#         self.course_name=course_name
#
#     def pri1(self):
#         print(f"name of course={self.course_name}")
#
#
#
# class branch(univercity):
#     def __init__(self,univ_name,branches):
#         univercity.__init__(self, univ_name)
#         self.branches=branches
#
#     def pri2(self):
#         print(f"name of branch={self.branches}")
#
#
# class student(course,branch):
#     def __init__(self,univ_name,course_name,branches,student_name):
#         course.__init__(self,univ_name,course_name)
#         branch.__init__(self,univ_name,branches)
#         self.student_name=student_name
#
#     def pri3(self):
#         print(f"studentname={self.student_name}")
#
# obj=student("mg univercity","b.com","taxation","abin c joseph")
#
# obj.pri()
# obj.pri1()
# obj.pri2()
# obj.pri3()


# class univercity():
#     def setval(self,univ_name):
#         self.univ_name=univ_name
#
#     def pri(self):
#         print("name of univercity=",self.univ_name)
#         print(f"name of univercity= {self.univ_name}")
#
#
#
# class course(univercity):
#     def setval1(self,course_name):
#         self.course_name=course_name
#
#     def pri1(self):
#         print(f"name of course={self.course_name}")
#
#
#
# class branch(univercity):
#     def setval2(self,branches):
#         self.branches=branches
#
#     def pri2(self):
#         print(f"name of branch={self.branches}")
#
#
# class student(course,branch):
#     def setval3(self,student_name):
#         self.student_name=student_name
#
#     def pri3(self):
#         print(f"studentname={self.student_name}")
#
# obj=student()
#
# obj.setval("mg univercity")
# obj.pri()
#
# obj.setval1("b.com")
# obj.pri1()
#
# obj.setval2("tax")
# obj.pri2()
#
# obj.setval3("abin")
# obj.pri3()