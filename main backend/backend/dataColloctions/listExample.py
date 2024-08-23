# li=[1,1,2,"abin",2,'t','t']
# for i in li:
#     print(i)

#
# li=[1,2,3,4,5,6,7,8,9]
# for i in li:
#     if i%2==0:
#         print(i)

# first letter a

# first letter "a" printing program
# name=['abin','sabin','Akhil','jiffin','joby','joseph','albin']
# b = "a"
# for i in name:
#     if i[0] == b:
#         print(i)


# # first letter "a" and "A" printing program
# name=['abin','sabin','Akhil','jiffin','joby','joseph','albin']
#
# for i in name:
#     if i[0] == "a" or i[0] == "A":
#         print(i)



# # any index should be a
# name=['abin','sabin','Akhil','jiffin','joby','joseph','albin']
#
# for i in name:
#     if "a" in i:
#         print(i)

# functions of list

# a=['abin','sabin','Akhil','jiffin','joby','joseph','albin']

# a.append(2)
# print(a)

# a.insert(4,"john")
# print(a)

# a.extend([25,"dc","35"])
# print(a)

# a.pop(3)
# print(a)

# a.remove("joby")
# print(a)

# print(a[-1])

# print(a.index("jiffin"))


# 2 list chernne mattoru list akunnu
# /////////////////////////////////////
# a=['abin','sabin','Akhil','jiffin','joby','joseph','albin']
# b=[25,"dc","35"]

#
# creating a new list to removing morethan one values
c=['amal','albert','gokul','anadhu','rohith','amarnath',35,35,'ajay','amal','anadhu']
b=[]
for i in c:
    if i not in b:
        b.append(i)
print(b)