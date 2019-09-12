# a = int(input("Tell me one number: "))
# b = int(input("Tell me another number: "))
# print("a/b = ", a/b)
# print("a+b = ", a+b)


try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a / b)
    print("a+b = ", a + b)
except:
    print("Bug in user input.")

