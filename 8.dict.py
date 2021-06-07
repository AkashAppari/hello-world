thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

x= thisdict["model"]
print(x)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.get("model")
print(x)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["year"]=2018
print(thisdict)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)
    
for x,y in thisdict.items():
    print(x,y)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["colour"]="red"
print(thisdict)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.pop("model")
print(thisdict)


thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.clear()
print(thisdict)
