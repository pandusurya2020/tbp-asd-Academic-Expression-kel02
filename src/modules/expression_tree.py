import math
from typing import Optional, Dict, List

# Definisi Node Pohon Ekspresi sesuai panduan [5]
class ExprNode:
    """Node untuk Binary Expression Tree.
    Node internal menyimpan operator/fungsi, daun menyimpan operand/variabel [2].
    """
    def __init__(self, val: str):
        self.val = val
        self.left: Optional['ExprNode'] = None
        self.right: Optional['ExprNode'] = None

# Fungsi untuk membangun pohon dari postfix [5, 6]
def build_expr_tree(postfix: List[str]) -> Optional[ExprNode]:
    """
    Membangun binary expression tree dari token postfix menggunakan Stack.
    Big-O: O(n) [2, 7].
    """
    # Menggunakan list Python sebagai Stack sederhana untuk demo [6]
    stack = []
    
    # Operator biner dan fungsi unary dari spesifikasi sistem [8, 9]
    operators = {'+', '-', '*', '/', '^'}
    functions = {'sin', 'cos', 'sqrt', 'log', 'abs'}

    for tok in postfix:
        node = ExprNode(tok)
        if tok in operators:
            # Operator biner: ambil dua operand (kanan dulu baru kiri) [10, 11]
            node.right = stack.pop()
            node.left = stack.pop()
        elif tok in functions:
            # Fungsi unary: hanya mengambil satu operand (sebagai anak kanan) [12]
            node.right = stack.pop()
            
        stack.append(node)
        
    return stack.pop() if stack else None

# Implementasi Traversal Pohon [12]
def inorder_expr(node: Optional[ExprNode]) -> str:
    """Traversal Inorder: Menghasilkan infix notation dengan kurung [2]."""
    if node is None: return ""
    if node.left is None and node.right is None:
        return str(node.val)
    
    # Rekursi dengan penambahan kurung untuk kejelasan precedence [1]
    res = "(" + inorder_expr(node.left) + str(node.val) + inorder_expr(node.right) + ")"
    return res.replace("None", "") # Menangani struktur fungsi unary

def preorder_expr(node: Optional[ExprNode]) -> List[str]:
    """Traversal Preorder: Menghasilkan prefix notation [2, 13]."""
    if node is None: return []
    return [node.val] + preorder_expr(node.left) + preorder_expr(node.right)

def postorder_expr(node: Optional[ExprNode]) -> List[str]:
    """Traversal Postorder: Menghasilkan postfix notation [2, 14]."""
    if node is None: return []
    return postorder_expr(node.left) + postorder_expr(node.right) + [node.val]

# Evaluasi Rekursif Pohon [15, 16]
def eval_tree(node: Optional[ExprNode], var_table: Dict[str, float]) -> float:
    """
    Evaluasi numerik pohon ekspresi secara rekursif (Postorder).
    Big-O: O(n) [2, 16].
    """
    if node is None: return 0.0
    
    # Kasus Daun: Angka atau Variabel [17]
    if node.left is None and node.right is None:
        try:
            return float(node.val)
        except ValueError:
            # Lookup nilai variabel dari tabel (BST) [2, 18]
            val = var_table.get(node.val)
            if val is None: raise ValueError(f"Variabel '{node.val}' belum di-SET")
            return val

    # Rekursi nilai anak [17]
    left_val = eval_tree(node.left, var_table)
    right_val = eval_tree(node.right, var_table)
    op = node.val

    # Logika Operasi [9, 17]
    if op == '+': return left_val + right_val
    elif op == '-': return left_val - right_val
    elif op == '*': return left_val * right_val
    elif op == '/': return left_val / right_val
    elif op == '^': return left_val ** right_val
    elif op == 'sin': return math.sin(right_val)
    elif op == 'cos': return math.cos(right_val)
    elif op == 'sqrt': return math.sqrt(right_val)
    elif op == 'log': return math.log(right_val) if right_val > 0 else 0
    elif op == 'abs': return abs(right_val)
    
    return 0.0

# Blok Driver untuk menjalankan kode secara mandiri [3, 19]
if __name__ == "__main__":
    print("=== Demo Modul Expression Tree (Kelompok 02) ===")
    
    # Contoh postfix dari ekspresi infix: (a + 5) * 2
    sample_postfix = ['a', '5', '+', '2', '*']
    sample_vars = {'a': 10.0} # Simulasi BST Tabel Variabel [20]

    try:
        # 1. Membangun Pohon
        root = build_expr_tree(sample_postfix)
        print(f"Postfix Input: {sample_postfix}")
        
        # 2. Menampilkan Hasil Traversal
        print(f"Inorder (Infix)   : {inorder_expr(root)}")
        print(f"Preorder (Prefix) : {' '.join(preorder_expr(root))}")
        print(f"Postorder (Postfix): {' '.join(postorder_expr(root))}")
        
        # 3. Evaluasi
        result = eval_tree(root, sample_vars)
        print(f"Hasil Evaluasi (a=10): {result}")
        
    except Exception as e:
        print(f"Error: {e}")