from typing import Optional, List, Tuple

class VarBSTNode:
    """Node untuk menyimpan variabel. Big-O Ruang: O(1)."""
    def __init__(self, key: str, val: float):
        self.key = key
        self.val = val
        self.left: Optional['VarBSTNode'] = None
        self.right: Optional['VarBSTNode'] = None

class VarBST:
    """
    Implementasi Binary Search Tree untuk Tabel Variabel (Symbol Table).
    Dibangun murni tanpa library eksternal sesuai Panduan TBP [4].
    """
    def __init__(self):
        """Inisialisasi BST kosong. Big-O: O(1)."""
        self.root: Optional[VarBSTNode] = None

    def set(self, key: str, val: float):
        """
        Menyisipkan variabel baru atau memperbarui nilai jika key sudah ada.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n) jika pohon miring [1].
        """
        if self.root is None:
            self.root = VarBSTNode(key, val)
        else:
            self._subtree_set(self.root, key, val)

    def _subtree_set(self, p, key, val):
        """Helper rekursif untuk penyisipan node (Goodrich, Code Fragment 11.3)."""
        if key == p.key:
            p.val = val  # Update nilai jika kunci sudah ada
        elif key < p.key:
            if p.left is None:
                p.left = VarBSTNode(key, val)
            else:
                self._subtree_set(p.left, key, val)
        else:
            if p.right is None:
                p.right = VarBSTNode(key, val)
            else:
                self._subtree_set(p.right, key, val)

    def get(self, key: str) -> Optional[float]:
        """
        Mencari nilai variabel berdasarkan key.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n) [1].
        """
        node = self._subtree_search(self.root, key)
        return node.val if node is not None else None

    def _subtree_search(self, p, key):
        """Helper rekursif untuk pencarian node (Goodrich, Code Fragment 11.2)."""
        if p is None:
            return None
        if key == p.key:
            return p
        elif key < p.key:
            return self._subtree_search(p.left, key)
        else:
            return self._subtree_search(p.right, key)

    def delete(self, key: str):
        """
        Menghapus variabel dari tabel (Fitur wajib Topic 5 [5]).
        Big-O Waktu: Rata-rata O(log n) [1].
        """
        self.root = self._subtree_delete(self.root, key)

    def _subtree_delete(self, p, key):
        """Helper rekursif penghapusan dengan logika Inorder Successor [6]."""
        if p is None: return None
        if key < p.key:
            p.left = self._subtree_delete(p.left, key)
        elif key > p.key:
            p.right = self._subtree_delete(p.right, key)
        else:
            # Skenario 1 & 2: Node dengan 0 atau 1 anak
            if p.left is None: return p.right
            if p.right is None: return p.left
            # Skenario 3: Node dengan 2 anak
            temp = self._min_node(p.right)
            p.key, p.val = temp.key, temp.val
            p.right = self._subtree_delete(p.right, temp.key)
        return p

    def _min_node(self, p):
        """Mencari node terkecil untuk membantu operasi delete [7]."""
        curr = p
        while curr.left is not None:
            curr = curr.left
        return curr

    def list_all(self) -> List[Tuple[str, float]]:
        """
        Menghasilkan list (key, value) yang terurut alfabetis.
        Big-O Waktu: O(n) karena mengunjungi setiap node satu kali [8].
        """
        result = []
        self._subtree_inorder(self.root, result)
        return result

    def _subtree_inorder(self, p, result):
        """Helper rekursif untuk traversal inorder (Goodrich, Code Fragment 8.15)."""
        if p is not None:
            self._subtree_inorder(p.left, result)
            result.append((p.key, p.val))
            self._subtree_inorder(p.right, result)

# ─── ANTARMUKA CLI INTERAKTIF (SESUAI PANDUAN TBP) ───
def main():
    bst = VarBST()
    print("--- Academic Expression Evaluator: Tabel Variabel ---")
    print("Perintah: SET <var> <val> | GET <var> | DELETE <var> | LIST | KELUAR")

    while True:
        try:
            line = input("\n>> ").strip()
            if not line: continue
            
            parts = line.split()
            cmd = parts[0].upper() # Ambil elemen string indeks 0 agar tidak AttributeError

            if cmd == "SET" and len(parts) == 3:
                var, val = parts[9], float(parts[10])
                bst.set(var, val)
                print(f"Hasil: OK [{var}={val}] (Big-O: O(log n))")

            elif cmd == "GET" and len(parts) == 2:
                var = parts[9]
                res = bst.get(var)
                if res is not None:
                    print(f"Hasil: {var} = {res} (Big-O: O(log n))")
                else:
                    print(f"Error: Variabel '{var}' tidak ditemukan. (Big-O: O(log n))")

            elif cmd == "DELETE" and len(parts) == 2:
                var = parts[9]
                bst.delete(var)
                print(f"Hasil: '{var}' dihapus (Big-O: O(log n))")

            elif cmd == "LIST":
                items = bst.list_all()
                print("Daftar Variabel (Terurut Alfabetis):")
                if not items: print("  (Kosong)")
                for k, v in items:
                    print(f"  {k} : {v}")
                print("Analisis: Traversal Inorder (Big-O: O(n))")

            elif cmd == "KELUAR":
                print("Selesai.")
                break
            else:
                print("Error: Perintah tidak dikenal atau argumen salah.")

        except ValueError:
            print("Error: Nilai harus berupa angka numerik!")
        except Exception as e:
            print(f"Sistem Error: {e}")

if __name__ == "__main__":
    # Menjalankan pengujian otomatis dengan data baru (Konstanta Sains)
    bst_test = VarBST()
    # Data pengujian unik: Golden Ratio (phi), Avogadro (Na), Boltzmann (k)
    print("--- Menjalankan Uji BST Otomatis ---")
    bst_test.set("phi", 1.618)
    bst_test.set("Na", 6.022)
    bst_test.set("k", 1.380)
    
    print(f"Pencarian 'phi': {bst_test.get('phi')} (Big-O: O(log n))")
    
    print("\nDaftar variabel (Inorder):")
    for key, val in bst_test.list_all():
        print(f" {key} = {val}")
    
    print("\n--- Berpindah ke Mode CLI Interaktif ---")
    main()