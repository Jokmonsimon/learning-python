# Example file for working with exceptions
# LinkedIn Learning Python course by Joe Marini

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10 / 0

# TODO: Exceptions provide a way of catching errors and then  them 
# in a separate section of the code to group them together
try:
    x = 10 / 0
except:
    print("Oops! That didn't work!")
# TODO: You can also catch specific exceptions
try:
    answer = input("Please enter the number to divide by 10? ")
    num = int(answer)
    print(10/num)

except ZeroDivisionError as e:
    print("You cannot divide by zero")

except ValueError as e:
    print("You entered invalid number!")
    print(e)

finally:
    print("This code always runs!")
    