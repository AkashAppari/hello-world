thisset={"apple","banana","cherry"}

print(thisset)

for x in thisset:
    print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)


thisset={"apple","banana","cherry"}

thisset.update(["orange","mango","grapes"])
print(thisset)


thisset={"apple","banana","cherry"}

print(len(thisset))

thisset.remove("banana")
print(thisset)


thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)


thisset={"apple","banana","cherry"}

x=thisset.pop()
print(x)
print(thisset)


thisset={"apple","banana","cherry"}

thisset.clear()
print(thisset)
