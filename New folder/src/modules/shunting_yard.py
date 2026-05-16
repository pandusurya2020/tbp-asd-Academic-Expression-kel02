import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

# Aturan kekuatan operator matematika
PREC = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
RASSOC = {'^'}  # Pangkat dikerjakan dari kanan

def infix_to_postfix(tokens: list) -> list:
    """Mengubah rumus infix menjadi postfix menggunakan Stack."""
    output = []
    op_stack = Stack()  # Memanggil Stack berbasis Linked List yang kamu buat tadi

    for tok in tokens:
        if tok.isalnum() and tok not in PREC:
            output.append(tok)
        elif tok == '(':
            op_stack.push(tok)
        elif tok == ')':
            while not op_stack.is_empty() and op_stack.peek() != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # Buang kurung buka '('
        elif tok in PREC:
            while (not op_stack.is_empty() and op_stack.peek() != '(' and
                   (PREC[op_stack.peek()] > PREC[tok] or 
                   (PREC[op_stack.peek()] == PREC[tok] and tok not in RASSOC))):
                output.append(op_stack.pop())
            op_stack.push(tok)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output