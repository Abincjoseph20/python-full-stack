# return statment is used to end the exicution of the function called return
#
# x = int(input("enter a number:"))
# y = int(input("enter a number:"))
# def add(x,y):
#     return (x+y)
# print(add(x,y))




# recursion
# function called its self
# -----------------------------

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         f=n*fact(n-1)
#         return f
# print(fact(4))


# fibinoci using recursion

n=int(input("enter a number: "))
def fib(n):
    if n<=1:
        return n
    else:
        f=fib(n-1)+fib(n-2)
        return f
for i in range(n):
    print(fib(i))