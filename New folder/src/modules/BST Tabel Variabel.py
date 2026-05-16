class VarBSTNode:
    """
    Node untuk menyimpan data variabel dalam Tabel Variabel.
    Menyimpan kunci berupa string (nama variabel) dan nilai numerik (float).
    Kompleksitas Ruang: O(1) per node.
    """
    def __init__(self, key: str, val: float):
        self.key = key
        self.val = val
        self.left: Optional['VarBSTNode'] = None
        self.right: Optional['VarBSTNode'] = None

class VarBST:
    """
    Implementasi Binary Search Tree (BST) sebagai Symbol Table (Topik 5).
    Struktur data ini digunakan untuk menyimpan konstanta/variabel kalkulator.
    Algoritma merujuk pada referensi Goodrich dkk.
    """
    def __init__(self):
        """Inisialisasi pohon dengan root kosong. Big-O: O(1)."""
        self.root: Optional[VarBSTNode] = None

    def set(self, key: str, val: float):
        """
        Menyisipkan variabel baru atau memperbarui nilai jika kunci sudah ada.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n) jika data terurut. [3, 4]
        """
        self.root = self._subtree_set(self.root, key, val)

    def _subtree_set(self, p: Optional[VarBSTNode], key: str, val: float) -> VarBSTNode:
        """Helper rekursif untuk operasi penyisipan/update."""
        if p is None:
            return VarBSTNode(key, val)
        if key == p.key:
            p.val = val  # Update nilai jika variabel sudah ada
        elif key < p.key:
            p.left = self._subtree_set(p.left, key, val)
        else:
            p.right = self._subtree_set(p.right, key, val)
        return p

    def get(self, key: str) -> Optional[float]:
        """
        Mencari nilai variabel berdasarkan kunci.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n). [4]
        """
        node = self._subtree_search(self.root, key)
        return node.val if node else None

    def _subtree_search(self, p: Optional[VarBSTNode], key: str) -> Optional[VarBSTNode]:
        """Helper rekursif untuk pencarian data."""
        if p is None or p.key == key:
            return p
        if key < p.key:
            return self._subtree_search(p.left, key)
        return self._subtree_search(p.right, key)

    def delete(self, key: str):
        """
        Menghapus variabel dari tabel (Fitur wajib Topik 5).
        Big-O Waktu: Rata-rata O(log n). [3, 4]
        """
        self.root = self._subtree_delete(self.root, key)

    def _subtree_delete(self, p: Optional[VarBSTNode], key: str) -> Optional[VarBSTNode]:
        """Helper rekursif untuk penghapusan node (menangani 3 skenario anak)."""
        if p is None:
            return None
        
        if key < p.key:
            p.left = self._subtree_delete(p.left, key)
        elif key > p.key:
            p.right = self._subtree_delete(p.right, key)
        else:
            # Skenario 1 & 2: Node dengan 0 atau 1 anak
            if p.left is None: return p.right
            if p.right is None: return p.left
            
            # Skenario 3: Node dengan 2 anak (cari inorder successor)
            temp = self._min_node(p.right)
            p.key, p.val = temp.key, temp.val
            p.right = self._subtree_delete(p.right, temp.key)
        return p

    def _min_node(self, p: VarBSTNode) -> VarBSTNode:
        """Mencari node terkecil (paling kiri) di sub-pohon."""
        curr = p
        while curr.left is not None:
            curr = curr.left
        return curr

    def list_all(self) -> List[Tuple[str, float]]:
        """
        Menghasilkan daftar semua variabel terurut alfabetis (Inorder).
        Big-O Waktu: O(n) karena mengunjungi setiap node satu kali. [5]
        """
        res = []
        self._subtree_inorder(self.root, res)
        return res

    def _subtree_inorder(self, p: Optional[VarBSTNode], res: List[Tuple[str, float]]):
        """Helper rekursif traversal inorder."""
        if p:
            self._subtree_inorder(p.left, res)
            res.append((p.key, p.val))
            self._subtree_inorder(p.right, res)

def main():
    """Antarmuka CLI interaktif sesuai standar operasional Panduan TBP. [6, 7]"""
    bst = VarBST()
    print("--- Academic Expression Evaluator: Tabel Variabel ---")
    print("Format: SET <var> <val> | GET <var> | DELETE <var> | LIST | KELUAR")

    while True:
        try:
            line = input("\n>> ").strip()
            if not line: continue
            
            parts = line.split()
            cmd = parts.upper()

            if cmd == "SET" and len(parts) == 3:
                var, val = parts[1], float(parts[8])
                bst.set(var, val)
                print(f"Hasil: OK [{var}={val}] (Big-O: O(log n))")

            elif cmd == "GET" and len(parts) == 2:
                var = parts[1]
                res = bst.get(var)
                if res is not None:
                    print(f"Hasil: {var} = {res} (Big-O: O(log n))")
                else:
                    print(f"Error: Variabel '{var}' tidak ditemukan. (Big-O: O(log n))")

            elif cmd == "DELETE" and len(parts) == 2:
                var = parts[1]
                bst.delete(var)
                print(f"Hasil: '{var}' berhasil dihapus. (Big-O: O(log n))")

            elif cmd == "LIST":
                items = bst.list_all()
                print("Daftar Variabel (Terurut Alfabetis):")
                if not items:
                    print("  (Kosong)")
                for k, v in items:
                    print(f"  {k} : {v}")
                print("Analisis: Traversal Inorder (Big-O: O(n))")

            elif cmd == "KELUAR":
                print("Program dihentikan.")
                break
            else:
                print("Error: Perintah tidak dikenal atau argumen tidak lengkap.")

        except ValueError:
            print("Error: Input nilai harus berupa angka numerik!")
        except Exception as e:
            print(f"Sistem Error: {e}")

if __name__ == "__main__":
    main()