long: str = ""
while True:
    a: str = input("please enter the first string: ")
    b: str = input("please enter the second string: ")
    if a == b:
        break
    else:
        long = long + a + " " + b + " "
        print(long)
