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