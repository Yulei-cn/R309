def divEntier(x: int, y: int) -> int:
    if x < 0 or y < 0:
        raise ValueError("Both x and y must be non-negative integers.")
    if y == 0:
        raise ValueError("The value of y cannot be 0.")
    if x < y:
        return 0
    else:
        return divEntier(x - y, y) + 1

def main():
    while True:
        try:
            x = int(input("Enter the value of x: "))
            y = int(input("Enter the value of y: "))
            if y == 0:
                raise ValueError("The value of y cannot be 0.")
            result = divEntier(x, y)
            print(f"The integer division of {x} by {y} is {result}")
            break  # Exit the loop if input is valid
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
