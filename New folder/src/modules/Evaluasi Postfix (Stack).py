import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

def eval_postfix(postfix_tokens: list, var_bst=None) -> float:
    eval_stack = Stack()  # Stack untuk menampung angka perhitungan

    for tok in postfix_tokens:
        # Jika token berupa angka
        if tok.replace('.', '', 1).isdigit():
            eval_stack.push(float(tok))
        # Jika token berupa operator (+, -, *, /)
        elif tok in ['+', '-', '*', '/']:
            b = eval_stack.pop()
            a = eval_stack.pop()
            
            if tok == '+':
                eval_stack.push(a + b)
            elif tok == '-':
                eval_stack.push(a - b)
            elif tok == '*':
                eval_stack.push(a * b)
            elif tok == '/':
                eval_stack.push(a / b)

    return eval_stack.pop()  # Hasil akhir berada di tumpukan paling atas