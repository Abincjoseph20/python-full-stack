# iteration
# a="futuroitsolutions"
# for i in a:
#     print(i)

# a="futuroitsolutions"
# print(a.count("i"))

# repeated value
# a="futuroitsolutions"
# for i in a:
#     if a.count(i)>1:
#         print(i)

# repeated value
# a="futuroitsolutions"
# b=""
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b = b + i
# print(b)

# first repeated string
# doubt olla program

# a="futturoitsolutions"
# b=""
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b = b + i
#         elif i in b:
#             print(i)
#             break

# a="futturoitsolutions"
# b=""
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b = b + i
#         elif i in b:
#             print(i)
#             break

# secound repated string
# a="futturoitsolutions"
# b=""
# c=""
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b = b + i
#         else:
#             c = c + i
#
# print(b)
# print(c)
# print("secound repeted element is:",c[2])

# removing element

# a = "futturoitsolutions"
# b = input("Enter a character to remove: ")
# c = ""
# for i in a:
#     if i != b:
#         c = c + i
#         # c += i
# print(c)

# removing 2 elements

# a="futuroitsolutions"
# b=input("enter your elements: ")
# c=""
#
# for i in a:
#     if i not in b:
#         c = c + i
# print(c)

# removing wovels
#
# a="futuroitsolutions"
# b="aeiou"
# c=""
#
# for i in a:
#     if i not in b:
#         c = c + i
# print(c)

# last repeated elemet
#
# a="futuroitsolutions"
# b=""
# c=""
#
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b = b + i
#         else:
#             c = c + i
# print("last repeated element is ",c[-1])