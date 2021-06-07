#Pyhton arrays
cars=["Ford","Volvo","BMW"]

x=cars[0]
print(x)


x=len(cars)
print(x)

for x in cars:
    print(x)

cars.append("Honda")
for x in cars:
    print(x)

cars.pop(1)
for x in cars:
    print(x)

cars.remove("Volvo")
for x in cars:
    print(x)