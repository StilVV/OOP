n = int(input())


def print_row(size, row):
    print(f"{' ' * (size - row) + ('* ' * row)}")


def upper_rhombus(size):
    for row in range(1, size + 1):
        print_row(size, row)


def lower_rhombus(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def rhombus(size):
    upper_rhombus(size)
    lower_rhombus(size)


rhombus(n)
