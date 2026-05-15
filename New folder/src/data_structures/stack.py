# Shunting-Yard Algorithm Dijkstra (1961)
# Mengkonversi ekspresi infix → postfix menggunakan Stack.
# Kompleksitas: O(n) waktu, O(n) ruang.
#
# Aturan precedence:
# ^ : 4 (pangkat, right-associative)
# * : 3, / : 3 (kiri-asosiatif)
# + : 2, - : 2 (kiri-asosiatif)
# sin/cos/sqrt/log/abs : 5 (unary, right-associative)
#
# Algoritma (pseudocode):
# untuk setiap token t dalam ekspresi:
# jika t adalah angka/variabel: output(t)
# jika t adalah fungsi: push(t) ke operator_stack
# jika t adalah '(': push(t) ke operator_stack
# jika t adalah ')':
# while top != '(': output(pop())
# pop '(' (buang)
# jika top adalah fungsi: output(pop())
# jika t adalah operator:
# while (top adalah operator) dan
# (prec(top) > prec(t)) atau
# (prec(top) == prec(t) dan t left-assoc):
# output(pop())
# push(t)
# while operator_stack tidak kosong: output(pop())


import math, time
from typing import Optional, Dict, List, Tuple

# ── Precedence & associativity ─────────────────────────────────
PREC = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
RASSOC = {'^'} # right-associative operators
FUNCS = {'sin': math.sin, 'cos': math.cos, 'sqrt': math.sqrt,
'log': math.log, 'abs': abs}

# ── Node Linked List ──────────────────────────────────────────────
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None

# ── Stack berbasis Linked List ────────────────────────────────────
class Stack:
    def __init__(self):
        self.top: Optional[LLNode] = None
        self._size = 0
        
    def push(self, data) -> None:
        """Big-O: O(1)."""
        node = LLNode(data)
        node.next = self.top
        self.top = node
        self._size += 1
    
    def pop(self):
        """Big-O: O(1)."""
        if not self.top: return None
        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val
    
    def peek(self):
        return self.top.data if self.top else None
    
    def is_empty(self) -> bool:
        return self._size == 0