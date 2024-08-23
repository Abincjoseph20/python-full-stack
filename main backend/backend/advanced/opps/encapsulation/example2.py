# protectod


class student:
    def __init__(self,name,age):
        self._name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

stu=student("jose",30)

print("name:",stu._name,"age: ",stu.get_age())
stu.set_age(16)
print("name:",stu._name,"age:",stu.get_age())