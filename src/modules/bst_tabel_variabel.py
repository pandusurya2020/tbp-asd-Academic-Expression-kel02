# =================================================================
# BAGIAN 1: STRUKTUR DATA MURNI (Wajib implementasi dari nol)
# Sesuai referensi Goodrich dkk. dan Panduan TBP [Source 1, 2]
# =================================================================

class VarBSTNode:
    """
    Node untuk menyimpan data variabel dalam BST.
    Menyimpan pasangan kunci (string) dan nilai numerik (float).
    Kompleksitas Ruang: O(1) per node.
    """
    def __init__(self, key: str, val: float):
        self.key = key
        self.val = val
        self.left: Optional['VarBSTNode'] = None
        self.right: Optional['VarBSTNode'] = None

class VarBST:
    """
    Implementasi murni Binary Search Tree sebagai Symbol Table (Tabel Variabel).
    Digunakan untuk menyimpan konstanta kalkulator (Topik 5).
    """
    def __init__(self):
        """Inisialisasi pohon dengan root kosong. Big-O: O(1)."""
        self.root: Optional[VarBSTNode] = None

    def set(self, key: str, val: float) -> None:
        """
        Menyisipkan variabel baru atau memperbarui nilai jika kunci sudah ada.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n) jika data linear [3].
        """
        self.root = self._subtree_set(self.root, key, val)

    def _subtree_set(self, p: Optional[VarBSTNode], key: str, val: float) -> VarBSTNode:
        """Helper rekursif untuk penyisipan/update node [4]."""
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
        Mencari nilai variabel berdasarkan kunci nama.
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n) [3].
        """
        node = self._subtree_search(self.root, key)
        return node.val if node else None

    def _subtree_search(self, p: Optional[VarBSTNode], key: str) -> Optional[VarBSTNode]:
        """Helper rekursif untuk pencarian node [5]."""
        if p is None or p.key == key:
            return p
        if key < p.key:
            return self._subtree_search(p.left, key)
        return self._subtree_search(p.right, key)

    def delete(self, key: str) -> None:
        """
        Menghapus variabel dari tabel (Fitur wajib Topik 5) [6].
        Big-O Waktu: Rata-rata O(log n).
        """
        self.root = self._subtree_delete(self.root, key)

    def _subtree_delete(self, p: Optional[VarBSTNode], key: str) -> Optional[VarBSTNode]:
        """Helper rekursif untuk menghapus node dengan 3 skenario anak [7]."""
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
            successor = self._min_node(p.right)
            p.key, p.val = successor.key, successor.val
            p.right = self._subtree_delete(p.right, successor.key)
        return p

    def _min_node(self, p: VarBSTNode) -> VarBSTNode:
        """Mencari node terkecil (paling kiri) di sub-pohon."""
        curr = p
        while curr.left:
            curr = curr.left
        return curr

    def list_all(self) -> List[Tuple[str, float]]:
        """
        Menghasilkan daftar semua variabel terurut alfabetis (Inorder).
        Big-O Waktu: O(n) karena mengunjungi setiap node satu kali [6].
        """
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, p: Optional[VarBSTNode], res: List):
        """Helper rekursif traversal inorder [8]."""
        if p:
            self._inorder(p.left, res)
            res.append((p.key, p.val))
            self._inorder(p.right, res)

# =================================================================
# BAGIAN 2: MODUL APLIKASI (INTERFANCE CLI)
# Syarat Skor 4: Interaktif & Menampilkan Analisis Big-O [1, 9]
# =================================================================

def main():
    """
    Entry point untuk Modul Tabel Variabel.
    Mendukung operasi SET, GET, DELETE, dan LIST secara interaktif.
    """
    bst = VarBST()
    print("\n" + "="*50)
    print("   ACADEMIC EXPRESSION EVALUATOR: SYMBOL TABLE")
    print("   Topik 5 - Kelompok 02")
    print("="*50)
    print("Format: SET <var> <val> | GET <var> | DELETE <var> | LIST | KELUAR")

    while True:
        try:
            line = input("\n>> ").strip()
            if not line:
                continue
            
            parts = line.split()
            cmd = parts.upper() # Perintah bersifat case-insensitive

            if cmd == "SET" and len(parts) == 3:
                var, val = parts[10], float(parts[11])
                bst.set(var, val)
                print(f"Hasil: OK [{var} = {val}]")
                print("Analisis Big-O: Operasi INSERT/UPDATE BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "GET" and len(parts) == 2:
                var = parts[10]
                res = bst.get(var)
                if res is not None:
                    print(f"Hasil: {var} = {res}")
                else:
                    print(f"Error: Variabel '{var}' tidak ditemukan.")
                print("Analisis Big-O: Operasi SEARCH BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "DELETE" and len(parts) == 2:
                var = parts[10]
                bst.delete(var)
                print(f"Hasil: Perintah hapus untuk '{var}' berhasil dieksekusi.")
                print("Analisis Big-O: Operasi DELETE BST - Kompleksitas: Rata-rata O(log n)")

            elif cmd == "LIST":
                items = bst.list_all()
                print("Daftar Variabel (Terurut Alfabetis):")
                if not items:
                    print("  (Kosong)")
                else:
                    for k, v in items:
                        print(f"  {k} : {v}")
                print(f"Analisis Big-O: Traversal Inorder mengunjungi {len(items)} node - Kompleksitas: O(n)")

            elif cmd == "KELUAR":
                print("Sistem dihentikan. Terima kasih.")
                break
            
            else:
                print("Kesalahan: Perintah tidak dikenal atau format salah.")

        except ValueError:
            print("Kesalahan: Input nilai harus berupa angka (numerik)!")
        except Exception as e:
            print(f"Sistem Error: {e}")

if __name__ == "__main__":
    main()