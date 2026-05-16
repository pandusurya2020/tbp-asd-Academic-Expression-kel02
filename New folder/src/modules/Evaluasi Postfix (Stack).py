import math

from src.data_structures.stack import Stack


# Operator yang didukung
OPERATORS = ['+', '-', '*', '/', '^']

# Fungsi yang didukung
FUNCTIONS = {
    'sin': math.sin,
    'cos': math.cos,
    'sqrt': math.sqrt,
    'log': math.log,
    'abs': abs
}


def is_number(token):

    try:
        float(token)
        return True
    except:
        return False


def evaluate_postfix(tokens, variables=None):
    """
    Evaluasi ekspresi postfix menggunakan Stack Linked List

    Big-O: O(n)
    """

    if variables is None:
        variables = {}

    stack = Stack()

    for token in tokens:

        # =========================
        # ANGKA
        # =========================
        if is_number(token):

            stack.push(float(token))

        # =========================
        # VARIABEL
        # =========================
        elif token.isalpha() and token not in FUNCTIONS:

            if token not in variables:
                raise ValueError(f"Variable '{token}' is not defined")

            stack.push(float(variables[token]))

        # =========================
        # FUNGSI
        # =========================
        elif token in FUNCTIONS:

            value = stack.pop()

            if value is None:
                raise ValueError("Invalid postfix expression")

            result = FUNCTIONS[token](value)

            stack.push(result)

        # =========================
        # OPERATOR
        # =========================
        elif token in OPERATORS:

            b = stack.pop()
            a = stack.pop()

            if a is None or b is None:
                raise ValueError("Invalid postfix expression")

            if token == '+':
                result = a + b

            elif token == '-':
                result = a - b

            elif token == '*':
                result = a * b

            elif token == '/':
                result = a / b

            elif token == '^':
                result = a ** b

            stack.push(result)

        else:
            raise ValueError(f"Unknown token: {token}")

    final_result = stack.pop()

    if not stack.is_empty():
        raise ValueError("Invalid postfix expression")

    return final_result