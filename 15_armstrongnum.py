#CHECK FOR ARMSTRING NUMBER
a=int(input("Enter NUMBER: "))
sum=0
num=a
while num>0:
    b=num%10
    sum+=b**3
    num//=10
if a==sum:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")