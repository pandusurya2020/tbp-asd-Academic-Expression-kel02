class VarBSTNode:
    """Node untuk menyimpan variabel. Kompleksitas Ruang: O(1)."""
    def __init__(self, key: str, val: float):
        self.key = key
        self.val = val
        self.left: Optional['VarBSTNode'] = None
        self.right: Optional['VarBSTNode'] = None

class VarBST:
    """Implementasi Binary Search Tree untuk Tabel Variabel."""
    def __init__(self):
        self.root: Optional[VarBSTNode] = None

    def set(self, key: str, val: float):
        """Menyisipkan/update variabel. Big-O: Rata-rata O(log n)."""
        self.root = self._subtree_set(self.root, key, val)

    def _subtree_set(self, p, key, val):
        if p is None: return VarBSTNode(key, val)
        if key == p.key: p.val = val
        elif key < p.key: p.left = self._subtree_set(p.left, key, val)
        else: p.right = self._subtree_set(p.right, key, val)
        return p

    def get(self, key: str) -> Optional[float]:
        """Mencari nilai variabel. Big-O: Rata-rata O(log n)."""
        node = self._subtree_search(self.root, key)
        return node.val if node else None

    def _subtree_search(self, p, key):
        if p is None or p.key == key: return p
        return self._subtree_search(p.left if key < p.key else p.right, key)

    def delete(self, key: str):
        """Menghapus variabel. Big-O: Rata-rata O(log n)."""
        self.root = self._subtree_delete(self.root, key)

    def _subtree_delete(self, p, key):
        if p is None: return None
        if key < p.key: p.left = self._subtree_delete(p.left, key)
        elif key > p.key: p.right = self._subtree_delete(p.right, key)
        else:
            if p.left is None: return p.right
            if p.right is None: return p.left
            successor = self._min_node(p.right)
            p.key, p.val = successor.key, successor.val
            p.right = self._subtree_delete(p.right, successor.key)
        return p

    def _min_node(self, p):
        curr = p
        while curr.left: curr = curr.left
        return curr

    def list_all(self) -> List[Tuple[str, float]]:
        """Daftar variabel terurut. Big-O: O(n)."""
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, p, res):
        if p:
            self._inorder(p.left, res)
            res.append((p.key, p.val))
            self._inorder(p.right, res)

# =================================================================
# BAGIAN 2: MODUL APLIKASI (INTERFACE CLI)
# =================================================================

def main():
    """Antarmuka CLI interaktif sesuai standar Panduan TBP."""
    bst = VarBST()
    print("\n" + "="*50)
    print("   ACADEMIC EXPRESSION EVALUATOR: SYMBOL TABLE")
    print("="*50)
    print("Format: SET <var> <val> | GET <var> | DELETE <var> | LIST | KELUAR")

    while True:
        try:
            line = input("\n>> ").strip()
            if not line: continue
            
            parts = line.split()
            cmd = parts.upper() # Perbaikan: akses indeks 0 untuk command

            if cmd == "SET" and len(parts) == 3:
                var, val = parts[3], float(parts[1])
                bst.set(var, val)
                print(f"Hasil: OK [{var} = {val}]")
                print("Analisis: Operasi INSERT/UPDATE BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "GET" and len(parts) == 2:
                var = parts[3]
                res = bst.get(var)
                status = f"{var} = {res}" if res is not None else f"Error: '{var}' tidak ditemukan"
                print(f"Hasil: {status}")
                print("Analisis: Operasi SEARCH BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "DELETE" and len(parts) == 2:
                var = parts[3]
                bst.delete(var)
                print(f"Hasil: Perintah hapus untuk '{var}' diproses.")
                print("Analisis: Operasi DELETE BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "LIST":
                items = bst.list_all()
                print("Daftar Variabel (Terurut Alfabetis):")
                if not items: print("  (Kosong)")
                else:
                    for k, v in items: print(f"  {k} : {v}")
                print(f"Analisis: Traversal Inorder ({len(items)} node) - Kompleksitas: O(n)")

            elif cmd == "KELUAR":
                print("Program dihentikan.")
                break
            else:
                print("Error: Format perintah salah atau tidak dikenal.")

        except ValueError:
            print("Error: Nilai variabel harus berupa angka numerik!")
        except Exception as e:
            print(f"Sistem Error: {e}")

if __name__ == "__main__":
    main()