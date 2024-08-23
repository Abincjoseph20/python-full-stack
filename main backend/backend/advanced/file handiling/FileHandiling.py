# w = new file create cheyyanum create aya file over write cheyyanum vendi use cheyyunnu

# f = open("sample.txt","w")
# f.write("learn python programming")
# f.close()


# a=uppend  cheyyan

# f = open("sample.txt","a")
# f.write("learn python programming \n")
# f.close()


# r=read cheyan

# f = open("sample.txt","r")
# read = f.read()
# print(read)
# f.close()

# x= create cheyyan

# file = open("text.txt",'a+')
# for i in file:
#     print(i)
# file.write("sindhu")
# print(file.read())
# file.close()

# f = open("filename.csv","w")
#
# f.close()

#import csv
#
# with open("filename.csv",mode='r')as file:
#     csvfile=csv.reader(file)
#
#     for lines in csvfile:
#         print(lines)
#         print(type(lines))

import csv

field=['name','branch','year']
rows=[['sanjay','cs',2021],['sindhu','cs',2020],['ragi','cs',2022]]
file_name='univercity_record.csv'
with open(file_name,'w',newline="")as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    for i in rows:
        csvwriter.writerow(i)

