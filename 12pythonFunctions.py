#py functions

def my_function():
    print("Hello from a funtion")
my_function()

print("")

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("")

def my_function(country="Norway"):
    print("I am from "+country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("")

def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)

print("")

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

print("")