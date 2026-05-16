import sys
import os

# Sinkronisasi path agar Python mendeteksi folder data_structures
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

def eval_postfix(postfix_tokens: list, var_bst=None) -> float:
    """Mengevaluasi dan menghitung nilai dari ekspresi postfix (O(n))."""
    eval_stack = Stack()

    for tok in postfix_tokens:
        # Cek jika token berbentuk angka numerik desimal/bulat
        if tok.replace('.', '', 1).isdigit():
            eval_stack.push(float(tok))
        elif tok in ['+', '-', '*', '/', '^']:
            b = eval_stack.pop()
            a = eval_stack.pop()
            
            if a is None or b is None:
                raise SyntaxError("Format ekspresi rumus matematika salah")

            if tok == '+':
                eval_stack.push(a + b)
            elif tok == '-':
                eval_stack.push(a - b)
            elif tok == '*':
                eval_stack.push(a * b)
            elif tok == '/':
                if b == 0:
                    raise ZeroDivisionError("Error: Pembagian dengan angka nol")
                eval_stack.push(a / b)
            elif tok == '^':
                eval_stack.push(a ** b)

    return eval_stack.pop()