# Example file for Python Conditional Structures
# LinkedIn Learning Python course by Joe Marini

def main():
    x, y = 289, 238

    # Conditional flow uses if, elif, else
    if x < y:
        print("The value {} is less than {}".format(x, y))
    elif x == y:
        print("The value {} is equal {}".format(x, y))
    else:
        print("The value {} is greater than {}".format(x, y))

    # Conditional statements let you use "a if C else b"
    result = "The value {} is less than {}".format(x, y) if x < y else "The value {} is greater or equal to {}".format(x, y)
    print(result)

    # Match-case makes it easy to compare multiple values
    value = "four"

    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)

if __name__ == "__main__":
    main()