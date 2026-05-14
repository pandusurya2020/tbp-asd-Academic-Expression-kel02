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
return output