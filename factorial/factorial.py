def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(f"Factorial from 7 = {factorial(7)}")
