import math


def triangular(x, a, b, c):
    if not (a < b < c):
        raise ValueError("Triangular function requires a < b < c.")

    if x <= a or x >= c:
        return 0.0
    if x <= b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)


def trapezoidal(x, a, b, c, d):
    if not (a < b <= c < d):
        raise ValueError("Trapezoidal function requires a < b <= c < d.")

    if x <= a or x >= d:
        return 0.0
    if x <= b:
        return (x - a) / (b - a)
    if x <= c:
        return 1.0
    return (d - x) / (d - c)


def gaussian(x, c, sigma):
    if sigma <= 0:
        raise ValueError("Gaussian function requires sigma > 0.")

    return math.exp(-((x - c) ** 2) / (2 * sigma ** 2))


def bell(x, a, b, c):
    if a == 0:
        raise ValueError("Bell function requires a != 0.")
    if b <= 0:
        raise ValueError("Bell function requires b > 0.")

    return 1 / (1 + abs((x - c) / a) ** (2 * b))


def sigmoid(x, a, c):
    if a == 0:
        raise ValueError("Sigmoid function requires a != 0.")

    return 1 / (1 + math.exp(-a * (x - c)))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def print_menu():
    print("\nChoose membership function:")
    print("'1' for Triangular")
    print("'2' for Trapezoidal")
    print("'3' for Gaussian")
    print("'4' for Bell Shape")
    print("'5' for Sigmoid")
    print("'0' to Exit")


def main():
    print("Fuzzy Membership Function Calculator")

    while True:
        print_menu()
        choice = input("Choice: ")

        if choice == "0":
            print("Program terminated.")
            break

        variable_name = input("Enter fuzzy variable name: ")
        x = get_float("Enter value to evaluate: ")

        try:
            if choice == "1":
                a = get_float("Enter left point (a): ")
                b = get_float("Enter peak point (b): ")
                c = get_float("Enter right point (c): ")
                result = triangular(x, a, b, c)
                function_type = "Triangular"

            elif choice == "2":
                a = get_float("Enter bottom-left point (a): ")
                b = get_float("Enter top-left point (b): ")
                c = get_float("Enter top-right point (c): ")
                d = get_float("Enter bottom-right point (d): ")
                result = trapezoidal(x, a, b, c, d)
                function_type = "Trapezoidal"

            elif choice == "3":
                c = get_float("Enter centre value (c): ")
                sigma = get_float("Enter spread value (sigma): ")
                result = gaussian(x, c, sigma)
                function_type = "Gaussian"

            elif choice == "4":
                a = get_float("Enter width value (a): ")
                b = get_float("Enter slope value (b): ")
                c = get_float("Enter centre value (c): ")
                result = bell(x, a, b, c)
                function_type = "Bell Shape"

            elif choice == "5":
                a = get_float("Enter slope value (a): ")
                c = get_float("Enter centre value (c): ")
                result = sigmoid(x, a, c)
                function_type = "Sigmoid"

            else:
                print("Invalid choice. Please try again.")
                continue

            print("\nResult")
            print("------")
            print(f"Variable name: {variable_name}")
            print(f"Function type: {function_type}")
            print(f"Crisp input x: {x}")
            print(f"Membership degree: {result:.4f}")

        except ValueError as error:
            print(f"Input error: {error}")


main()