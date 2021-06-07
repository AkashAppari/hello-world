#FIBONACCI SERIES
num=int(input("How many terms: "))
a=0
b=1
print("Fibonacci Series: ")
for i in range(0,num):
    print(a)
    c=a+b
    a=b
    b=c