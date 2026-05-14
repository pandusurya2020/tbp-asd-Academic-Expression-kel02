# ── Evaluasi postfix (implementasikan) ───────────────────────────
def eval_postfix(tokens: List[str], var_table: Dict[str, float]) -> float:
    """
    Evaluasi token postfix menggunakan Stack Linked List.
    Lookup variabel dari var_table (BST dalam implementasi penuh).
    Big-O: O(n).
    """
    stack = Stack()
    for tok in tokens:
        if tok in FUNCS:
            # TODO: pop satu operand, terapkan fungsi, push hasil
            pass
        elif tok in PREC: # operator binary
            # TODO: pop dua operand, hitung, push hasil
            # Perhatian: urutan pop! b = pop(), a = pop() → a OP b
            pass
        elif tok.replace('.','',1).lstrip('-').isdigit():
            stack.push(float(tok))
        else: # variabel
            val = var_table.get(tok)
            if val is None: raise ValueError(f'Variabel {tok!r} belum di-SET')
            stack.push(val)
result = stack.pop()
if not stack.is_empty(): raise ValueError('Ekspresi tidak valid')
return result
