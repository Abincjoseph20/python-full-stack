# directry

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# 15/3/24
# while True:
#     print(10)
#     break

# # using while loop printing 11 to 20 even numbers
#
# i = 9
# while i < 20:
#     i = i + 1
#     if i % 2 == 0:
#         print(i)

#
# i = 10
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1


# factorial of numbers

# a = int(input("enter a number: "))
# b = 1
# i = 1
# while i <= a:
#     b = b * i
#     i = i + 1
# print(b)


# ///string iteration///
#
# a="futuro it solutions"
# i = 0
# while i < len(a):
#     print(a[i])
#     # a of index number
#     i = i + 1


# ///5th element printing///

# a="futuroitsolutions"
# i = 0
#
# while i < 6:
#     print(a[i],end="")
#     i = i + 1


# ///element removing while loop///

# a="futuroitsolutions"
# i=0
# b=input("enter a element: ")
# c=""
#
# while i < len(a):
#     if a[i] != b:
#         c = c + a[i]
#     i = i + 1
# print(c)


# printing even number position index

a = "futuroitsolutions"
i = 0

while i < len(a):
    if i % 2 == 0:
        print(a[i], end="  ")
    i = i + 1