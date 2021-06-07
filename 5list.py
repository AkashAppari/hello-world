thislist=["apple","banana","cherry"]

print(thislist)

print(thislist[1])

print(thislist[-1])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]

print(thislist[2:5])

print(thislist[:4])


thislist=["apple","banana","cherry"]

thislist[1]="blackcurrant"
print(thislist)


thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)

if "apple" in thislist:
    print("Yes,'apple' is in the fruit list")

print(len(thislist))

thislist.append("orange")
print(thislist)


thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)


thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)


thislist=["apple","banana","cherry"]
thislist.pop()
print(thislist)


thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)


thislist=["apple","banana","cherry"]
del thislist #deletes the list


thislist=["apple","banana","cherry"]
thislist.clear()
print(thislist)

