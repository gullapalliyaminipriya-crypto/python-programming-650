
def hollow_diamond(n):
    # Upper half
    for i in range(1, n + 1):
        spaces = " " * (n - i)

        if i == 1:
            print(spaces + "*")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")

    # Lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)

        if i == 1:
            print(spaces + "*")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")


def symmetric_number_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        # Increasing numbers
        for j in range(1, i + 1):
            print(j, end="")

        # Decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()


def main():
    print("ADVANCED NUMERIC PATTERN GENERATOR")
    print("1. Hollow Diamond")
    print("2. Symmetric Number Pattern")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        n = int(input("Enter the size (positive integer): "))

        if n <= 0:
            print("Error: Size must be a positive integer.")
        elif choice == 1:
            print("\nHollow Diamond Pattern:")
            hollow_diamond(n)
        elif choice == 2:
            print("\nSymmetric Number Pattern:")
            symmetric_number_pattern(n)
        else:
            print("Error: Invalid pattern choice.")

    except ValueError:
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()

