# import mysql.connector
#
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",)
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")



# cursor() -> data ne process cheyyikkan ahne ex. insert cheytha data ne insert akkunnathe cursor() ahne


#table creation


# import mysql.connector
#
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="mydatabase"
# )
# print(mydb)
# mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE Customers(fname varchar(20),lname varchar(20))")


# show table

# import mysql.connector
#
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="abin"
# )
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
#
# for i in mycursor:
#     print(i)


# value insert

# import mysql.connector
#
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="mydatabase"
# )
# print(mydb)
# mycursor = mydb.cursor()
# a="INSERT INTO customers(fname,lname)VALUES(%s,%s)"
# b=('George','rajan')
#
# c="INSERT INTO customers(fname,lname)VALUES('diya','james')"
# print(a,b)
#
# mycursor.execute(a,b)
# mycursor.execute(c)
# mydb.commit()


# update

# import mysql.connector
#
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="mydatabase"
# )
# print(mydb)
# mycursor = mydb.cursor()
# mycursor.execute("UPDATE customers set lname='Mathew' WHERE lname='rajan'")
# mycursor.execute("commit")
#
# d=('diya',)
# mycursor.execute("DELETE FROM customers WHERE fname=%s",d)
# mycursor.execute("commit")
#


# drop

import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE customers")

