# Example file for Variables and Expressions
# LinkedIn Learning Python course by Joe Marini

# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries, Lists, Tuples
my_int = 502
my_float = 12.91
my_str = "My Learning Model"
my_bool = True
my_list = [0, 1, "Afande Ojok", 5.01, False]
my_tuple = (1, 3, 5, 7, 9)
my_dict = {"Course Intructor": "Afande Ojok","Course Name": "Introduction to Computer Literacy", "Description":"We believe by enrolling in this course, everyone can have access to online information"}

print(my_int) # Interger value
print(my_float) # Value with decimal point
print(my_str) # Sequence of characters
print(my_bool) # True or False
print(my_list) # Include any data type in square bracket
print(my_tuple) # Imutable - cannot be changed
print(my_dict) # Maps uniques keys to its pair values

# Re-declaring a variable
my_int = "Integer re-declared as string"
print(my_int)

# To access a member of a sequence type, use []
print(my_list[-4])
print(my_list[1])
print(my_list[0:2])
print(my_list[1:5:2])
print(my_tuple[1:4])