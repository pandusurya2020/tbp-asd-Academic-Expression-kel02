# ── Shunting-Yard: infix → postfix (implementasikan) ─────────────
def infix_to_postfix(tokens: List[str]) -> List[str]:
    """
    Konversi token infix ke postfix menggunakan Stack Linked List.
    Big-O: O(n) waktu, O(n) ruang.
    Catatan: unary minus belum didukung dalam starter ini.
    """
output: List[str] = []
op_stack = Stack()
# TODO: implementasikan Shunting-Yard Algorithm
# Gunakan PREC, RASSOC, FUNCS untuk panduan
PREC = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
RASSOC = {'^'} # right-associative operators
FUNCS = {'sin': math.sin, 'cos': math.cos, 'sqrt': math.sqrt,
'log': math.log, 'abs': abs}
return output