# Example file for Python Functions
# LinkedIn Learning Python course by Joe Marini

# TODO: Define a basic function
def func1():
    print("I am a function")

# TODO: Function that takes arguments
def func2(arg1, arg2):
    print(arg1," ", arg2)

# TODO: Function that returns a value
def cube(x):
    return x * x * x

# TODO: Function with default value for an argment
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# TODO: Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result    

func1
print(func1())
print(func1)

func2(10, 20)
print(func2(10, 20))

print(cube(3))

print(power(2))
print(power(2,3))
print(power(x=3, num=2))

print(multi_add(3, 1, 5, 7, 20))