import sys
import os

# Sinkronisasi path agar Python mendeteksi folder data_structures
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack

def eval_postfix(postfix_tokens: list, var_bst=None) -> float:
    """Mengevaluasi dan menghitung nilai dari ekspresi postfix (O(n))."""
    eval_stack = Stack()

    for tok in postfix_tokens:
        # 1. Cek jika token adalah huruf/variabel yang terdaftar di BST atau Dict kelompok
        if var_bst and hasattr(var_bst, 'get') and var_bst.get(tok) is not None:
            eval_stack.push(float(var_bst.get(tok)))
        elif var_bst and isinstance(var_bst, dict) and tok in var_bst:
            eval_stack.push(float(var_bst[tok]))
            
        # 2. Cek jika token berupa angka langsung (bisa positif, negatif, maupun desimal)
        else:
            try:
                # Menggunakan float() jauh lebih aman karena otomatis mendukung tanda minus (-)
                nilai_angka = float(tok)
                eval_stack.push(nilai_angka)
            except ValueError:
                # 3. Jika bukan angka/variabel, cek apakah ini operator matematika resmi
                if tok in ['+', '-', '*', '/', '^']:
                    b = eval_stack.pop()
                    a = eval_stack.pop()
                    
                    if a is None or b is None:
                        raise SyntaxError("Format ekspresi rumus matematika salah (kekurangan angka)")

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
                else:
                    # 4. Proteksi/Saringan terakhir jika ada variabel tidak dikenal atau typo karakter
                    raise NameError(f"Error: Variabel atau token '{tok}' tidak dikenali/belum terdaftar di BST")

    # Mengambil dan mengembalikan hasil kalkulasi final
    return eval_stack.pop()