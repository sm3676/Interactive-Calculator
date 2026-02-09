from calculator.operations import Calculator

def run_calculator():
    calc = Calculator()
    print("Welcome to Calculator")
    print("Operations: + - * /")
    print("Type exit to quit")

    while True:
        op = input("Enter operation: ")

        if op == "exit":
            print("Bye")
            break

        if op not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if op == "+":
                result = calc.add(a, b)
            elif op == "-":
                result = calc.subtract(a, b)
            elif op == "*":
                result = calc.multiply(a, b)
            else:
                result = calc.divide(a, b)

            print("Result:", result)

        except ValueError:
            print("Invalid number")
        except ZeroDivisionError as e:
            print(e)
