import sys
import os

# Sinkronisasi path agar Python mendeteksi folder data_structures
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

# Tingkat kekuatan hirarki operator matematika
PREC = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
RASSOC = {'^'}  # Pangkat dikerjakan dari kanan ke kiri

def infix_to_postfix(tokens: list) -> list:
    """Mengubah potongan token infix menjadi postfix menggunakan Stack (O(n))."""
    output = []
    op_stack = Stack()

    for tok in tokens:
        if tok.isalnum() and tok not in PREC:
            output.append(tok)
        elif tok == '(':
            op_stack.push(tok)
        elif tok == ')':
            while not op_stack.is_empty() and op_stack.peek() != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # Membuang tanda kurung buka '('
        elif tok in PREC:
            while (not op_stack.is_empty() and op_stack.peek() != '(' and
                   (PREC[op_stack.peek()] > PREC[tok] or 
                   (PREC[op_stack.peek()] == PREC[tok] and tok not in RASSOC))):
                output.append(op_stack.pop())
            op_stack.push(tok)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return output