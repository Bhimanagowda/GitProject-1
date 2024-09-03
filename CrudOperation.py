
a = float(input("Enter the First Number: "))
b = float(input("Enter the Second Number: "))


operation = input("Enter the operation (sum/diff/mul/div): ")

match operation:
    case "sum":
        c = a + b
        print(f"Sum of two numbers (a & b): {c}")
    case "diff":
        d = a - b
        print(f"Difference of two numbers (a & b): {d}")
    case "mul":
        e = a * b
        print(f"Multiplication of two numbers (a & b): {e}")
    case "div":
        if b != 0:
            f = a / b
            print(f"Division of two numbers (a & b): {f}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter 'sum', 'diff', 'mul', or 'div'.")
