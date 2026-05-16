<<<<<<< HEAD
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
=======
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

def eval_postfix(postfix_tokens: list, var_bst=None) -> float:
    """Menghitung hasil akhir dari rumus postfix menggunakan Stack."""
    eval_stack = Stack()

    for tok in postfix_tokens:
        # Jika token adalah angka
        if tok.replace('.', '', 1).isdigit():
            eval_stack.push(float(tok))
        # Jika token adalah operator, lakukan perhitungan
        elif tok in ['+', '-', '*', '/', '^']:
            b = eval_stack.pop()
            a = eval_stack.pop()
            
            if a is None or b is None:
                raise SyntaxError("Rumus tidak valid")

            if tok == '+':
                eval_stack.push(a + b)
            elif tok == '-':
                eval_stack.push(a - b)
            elif tok == '*':
                eval_stack.push(a * b)
            elif tok == '/':
                if b == 0:
                    raise ZeroDivisionError("Tidak bisa membagi dengan angka nol")
                eval_stack.push(a / b)
            elif tok == '^':
                eval_stack.push(a ** b)

    return eval_stack.pop()
>>>>>>> 8f2e3da00637e0cd1b1817cb2158ef9ca2df4a10
