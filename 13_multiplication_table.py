#MULTIPLICATION TABLE OF GIVEN NUMBER
a=int(input("Enter NUMBER whose multiplication table is to be displayed: "))
m=int(input("Enter the number of multiples required: "))
for i in range(1,m+1):
    b=a*i
    print(a,"x",i,"=",b)