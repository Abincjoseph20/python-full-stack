# zero divition error //- eppo 10/0 koduthal error ayi kanikkan ullla chance unde athane
#enagne undakunna problems ne pariharikkan upayogikkunna method ahne "try" and "except"
# try:
#     a = int(input("enter a number:-"))
#     b = int(input("enter a number:-"))
#
#     c = a / b
#     print(c)
# except:
#     print("enter a valid input")

# evde program stop aakathe veedum program nilkkan

# try:
#     a = int(input("enter a number:-"))
#     b = int(input("enter a number:-"))
#
#     c = a / b
# except:
#     print("enter a valid input")
# else:
#     print(c)


# finally enthe sambavichalum program run akum
#
# try:
#     a = int(input("enter a number:-"))
#     b = int(input("enter a number:-"))
#
#     c = a / b
# except:   #exception vannal mathram run akum
#     print("enter a valid input")
# else:   #exceptin vannilangil mathram run akum
#     print(c)
# finally:   #exeption vannalum vannillangilum program run akunnu
#     print("end of the program")

# correct input kodukkunna vare program run aaakan

while True:
    try:
        a = int(input("enter a number:-"))
        b = int(input("enter a number:-"))

        c = a / b
    except:
        print("enter a valid input")
    else:
        print(c)
        break