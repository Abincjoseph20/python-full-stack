# local scop of a variable
#
# def check_scop():
#
#     def do_local():
#         test="local test"
#
#     def non_local():
#         test="non_local test"
#
#     def do_global():
#         test=globals()
#
#     test="default"
#     do_local()
#     print("print value after do local:",test)
#
# check_scop()



# non_local scop of variable
#
# def check_scop():
#     def do_local():
#         test = "local test"
#
#     def non_local():
#         nonlocal test #non local ayal functionnde purathe acces cheyyan pattum
#         test = "non_local test"
#
#     def do_global():
#         test = "globals"
#
#
#     test = "default"
#     non_local()
#     print("print value after do local:", test)
#
# check_scop()


# global scop of variable
#
def check_scop():
    def do_local():
        test="local test"

    def non_local():
        nonlocal  test
        test="non_local test"

    def do_global():
        global  test
        test ="global"

    test="defalt"
    do_global()
    print("test value do local:",test)

check_scop()
print(test)
