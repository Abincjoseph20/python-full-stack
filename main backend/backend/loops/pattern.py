# n = int(input("enter:"))
#
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()
#


# for i in range(5):
#     for j in range(5):
#         print(" *", end="")
#     print()

#
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*",end=" ")
#     print()


# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()


#
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(n):
#         print(" *",end="")
#     print()



# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(n):
#         print("*",end="")
#     print()

# for i in range(n):
#     for j in range(n-i-1):
#         print("",end=" ")
#     for j in range(n):
#         print(" *",end="")
#     print()


# reverce pyramid
#
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print(" *",end="")
#     print()

# normal pyramid
#
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print(" *",end="")
#     print()

# rounded star
#
# n=6
# m=4
# for row in range(n):
#     for col in range(m):
#         if (row==0 or row ==5) and (col==1 or col==2):
#             print("*",end="")
#         elif (row > 1 or row < 4) and (col==0 or col==3):
#             print("*",end="")
#         else:
#             print("*",end="")
#     print()
#
# row = 6
# col = 4
# for i in range(0,row):
#     for j in range(0,col):
#         if((j==0 or j == col-1) and (i!=0 and i!=row-1)):
#             print("*",end="")
#         if ((i==0 or i==row-1) and (j==1 or j==2)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()


# for i in range(0,n):
#     for j in range(0,n):
#         if((i==0 or i==n-1) and (i==1 or j==n)):
#             print("*",end=" ")
#         else:
#             print(end="")
#     print()

n=3
for row in range(0,n):
    for col in range(0,n):
        if (row + col==1) or (row+col==3) or (row - col==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#for i in range(10):
#     print(i)

