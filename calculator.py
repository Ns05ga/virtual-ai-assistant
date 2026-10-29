import re


def parse_expression(command):
    
    pattern = r"^calculate\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)$"

    match = re.match(pattern, command.strip(), re.IGNORECASE)

    if not match:
        raise ValueError(
            "Use this format: calculate 12+8"
        )

    number1 = float(match.group(1))
    operator = match.group(2)
    number2 = float(match.group(3))

    return number1, operator, number2


def calculate(number1, operator, number2):
    
    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError(
                "I can't divide by zero — try a different number."
            )
        return number1 / number2

    else:
        raise ValueError("Unsupported operator.")
