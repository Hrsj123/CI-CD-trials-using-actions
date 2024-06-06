from rich.console import Console
from methods import (
    add,
    subtract,
    multiply,
    divide,
)


def main():
    console = Console()
    console.print("Hello", "World!", style="bold blue")

    num1, num2 = 1, 2
    res = add(num1, num2)
    console.print(f"Addition: {res}", style="bold green")
    res = subtract(num1, num2)
    console.print(f"Subtract: {res}", style="bold green")
    res = multiply(num1, num2)
    console.print(f"Multiply: {res}", style="bold green")
    res = divide(num1, num2)
    console.print(f"Divide: {res}", style="bold green")


if __name__ == '__main__':
    main()
