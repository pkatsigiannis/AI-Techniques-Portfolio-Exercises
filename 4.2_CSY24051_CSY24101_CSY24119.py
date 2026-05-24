import math
import matplotlib.pyplot as plt
import numpy as np


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


def get_plot_range(x, points):
    minimum = min(points)
    maximum = max(points)
    margin = (maximum - minimum) * 0.25

    if margin == 0:
        margin = abs(x) * 0.25 if x != 0 else 1

    return minimum - margin, maximum + margin


def display_graph(function_type, variable_name, x, result, x_values, y_values):
    plt.plot(x_values, y_values)
    plt.scatter(x, result)

    plt.title(f"{function_type} Membership Function - {variable_name}")
    plt.xlabel("Input value")
    plt.ylabel("Membership degree")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)

    plt.show()


def ask_to_display_graph(function_type, variable_name, x, result, x_values, y_values):
    choice = input("Display graph? (y/n): ").lower()

    if choice == "y":
        display_graph(function_type, variable_name, x, result, x_values, y_values)


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

                start, end = get_plot_range(x, [a, b, c, x])
                x_values = np.linspace(start, end, 500)
                y_values = [triangular(value, a, b, c) for value in x_values]

            elif choice == "2":
                a = get_float("Enter bottom-left point (a): ")
                b = get_float("Enter top-left point (b): ")
                c = get_float("Enter top-right point (c): ")
                d = get_float("Enter bottom-right point (d): ")

                result = trapezoidal(x, a, b, c, d)
                function_type = "Trapezoidal"

                start, end = get_plot_range(x, [a, b, c, d, x])
                x_values = np.linspace(start, end, 500)
                y_values = [trapezoidal(value, a, b, c, d) for value in x_values]

            elif choice == "3":
                c = get_float("Enter centre value (c): ")
                sigma = get_float("Enter spread value (sigma): ")

                result = gaussian(x, c, sigma)
                function_type = "Gaussian"

                start = min(x, c - 4 * sigma)
                end = max(x, c + 4 * sigma)
                x_values = np.linspace(start, end, 500)
                y_values = [gaussian(value, c, sigma) for value in x_values]

            elif choice == "4":
                a = get_float("Enter width value (a): ")
                b = get_float("Enter slope value (b): ")
                c = get_float("Enter centre value (c): ")

                result = bell(x, a, b, c)
                function_type = "Bell Shape"

                width = abs(a) * 4
                start = min(x, c - width)
                end = max(x, c + width)
                x_values = np.linspace(start, end, 500)
                y_values = [bell(value, a, b, c) for value in x_values]

            elif choice == "5":
                a = get_float("Enter slope value (a): ")
                c = get_float("Enter centre value (c): ")

                result = sigmoid(x, a, c)
                function_type = "Sigmoid"

                start, end = get_plot_range(x, [c - 10, c + 10, x])
                x_values = np.linspace(start, end, 500)
                y_values = [sigmoid(value, a, c) for value in x_values]

            else:
                print("Invalid choice. Please try again.")
                continue

            print("\nResult")
            print("------")
            print(f"Variable name: {variable_name}")
            print(f"Function type: {function_type}")
            print(f"Crisp input x: {x}")
            print(f"Membership degree: {result:.4f}")

            ask_to_display_graph(
                function_type,
                variable_name,
                x,
                result,
                x_values,
                y_values
            )

        except ValueError as error:
            print(f"Input error: {error}")


main()