#Factorial of a number using recursion
def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("Enter the number: "))

if num<0:
    print("Sorry, factorial does not exist for negative numbers")
    print("")
elif num==0:
    print("The factorial of 0 is 1")
    print("")
else:
    print("The factorial of ",num,"is",recur_factorial(num))
    print("")
