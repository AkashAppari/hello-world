#CHECK THE LARGEST OF THREE 
a=int(input("Enter Num1: "))
b=int(input("Enter Num2: "))
c=int(input("Enter Num3: "))
if a>b:
    if a>c:
        print(a,"is GREATEST!!!")
    else:
        print(c,"is GREATEST!!!")
else:
    if b>c:
        print(b,"is GREATEST!!!")
    else:
        print(c,"is GREATEST!!!")        