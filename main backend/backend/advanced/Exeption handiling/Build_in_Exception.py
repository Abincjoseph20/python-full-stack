# valu error-ValueError intiger ne pakaram string koduthal varunna error

# a = int(input("enter a number:-"))
# b = int(input("enter a number:-"))
#
# c = a / b
# print(c)

# Errors nde pere paranje konde programm cheyyunna reethi ahe ethe
# try:
#     a = int(input("enter a number:-"))
#     b = int(input("enter a number:-"))
#
#     c = a / b
# except ZeroDivisionError:
#     print("could not divesibl by '0'")
# except ValueError:
#     print("string object can't devise")
# else:
#     print(c)



while True:
    try:
        a = int(input("enter a number:-"))
        b = int(input("enter a number:-"))

        c = a / b
    except ZeroDivisionError:
        print("could not divesibl by '0'")
    except ValueError:
        print("string object can't devise")
    else:
        print(c)
        break