#SOLVE FOR QUADRATIC EQUATION
print("Quadratic Equation is:  ax^2+bx+c=0")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print("Entered Quadratic Equation is: " ,int(a),"x^2 + ",int(b),"x + ",int(c)," = 0")
r = b**2 - 4*a*c
###########################################################
# x1=((-b+((b**2)-4*a*c)**0.5)/(2*a))
# x2=((-b-((b**2)-4*a*c)**0.5)/(2*a))
# print(x1,x2)
###########################################################

if r > 0:
    num_roots = 2
    x1 = (((-b) + (r**0.5))/(2*a))     
    x2 = (((-b) - (r**0.5))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, as discriminant ", int(r), " is less than 0.")
    exit()

