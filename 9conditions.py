#IF
a=33
b=200
if b>a:
    print("b is greater than a")

print("")
#ELIF
a=33
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

print("")
#ELSE
a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print("")
#ELSE with IF
a=200
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is not greater than b")

print("")
#SHORTHAND IF
a=33
b=200
if a<b: print("a is greater than b")


a=2
b=330
print("A") if a>b else print("B")

print("")
#AND
a=200
b=33
c=500
if a>b and c>a:
    print("Both conditions are True")

print("")
#OR
a=200
b=33
c=500
if a>b or a>c:
    print("At least one of the conditions is True")
    
print("")
#NESTED IF
x=41
if x>10:
    print("Above tenn")
    if x>20:
        print("and also above 20!")
    else:
        print("bit not above 20.")

print("")
#PASS STATEMENT
a=33
b=200
if b>a:
    pass

print("")
#WHILE LOOP
i=1
while i<6:
    print(i)
    i+=1

print("")
#BREAK STATEMENT
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
print("")
#CONTINUE STATEMENT
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


print("")
#BREAK STATEMENT
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)


print("")
#CONTINUE STATEMENT
fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)