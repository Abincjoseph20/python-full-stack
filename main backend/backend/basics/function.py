# function defenition
# ----------------------
# function is a block of code to perform spesific task///

# def myfunction():
#     print( 10 + 20)
#
# myfunction()

# adding numbers using functions
#
# def myfunction():
#     a = int(input("enter 1st number : "))
#     b = int(input("enter 2nd number : "))
#     print( a + b)
# myfunction()

# function using arguments

# def myfunction(a,b):
#     print(a+b)
# myfunction("hi","hello")

#adding 2 numbers in function using arguments
#
# def myfunction(a,b):
#     print(a+b)
# x = int(input("enter 1st number:"))
# y = int(input("enter 2nd number:"))
# myfunction(x,y)


# `calculator using function and argument`

#
# x = int(input("enter 1st number : "))
# y = int(input("enter 2nd number : "))
# i = 0
# print("select the option:")
#
# def add(x,y):
#     print(x+y)
# def sub(x,y):
#      print(x-y)
#
# def div(x,y):
#     print(x/y)
#
# def mul(x,y):
#     print(x*y)
#
# while True:
#     a = int(input("select the option:1.add 2.sub 3.div 4.mul: 5:"))
#     if a == 1:
#         add(x,y)
#
#     elif a == 2:
#         sub(x,y)
#
#     elif a == 3:
#         div(x,y)
#
#     elif a == 4:
#         mul(x,y)
#
#     elif a == 5:
#         print("break")
#         break
#     else:
#         print("please enter a valid number")



# ATM programm

x =1000
def add(y):
    global x
    x = x + y
    print(x)
def sub(y):
    global x
    x = x - y
    print(x)
while True:
    a = int(input("enter the option: 1:withdrawal 2:deposit 3:balance enquiry 4:exit "))
    if a == 1:
        y = int(input("enter your amount: "))
        if y % 200 == 0 or y % 500 == 0:
            if y > x:
                print("you don't have enough balance")
            elif y <= x:
                sub(y)
    elif a == 2:
        y = int(input("enter your amount: "))
        add(y)
    elif a == 3:
        print("balance=",x)
    elif a == 4:
        print("you are exit your transaction")
        break
    else:
        print("please enter a valid option")