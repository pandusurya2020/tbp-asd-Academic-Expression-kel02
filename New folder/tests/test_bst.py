class VarBSTNode:
    def __init__(self, key: str, val: float):
        """Node untuk menyimpan variabel. Big-O Ruang: O(1)."""
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class VarBST:
    def __init__(self):
        """Inisialisasi BST kosong. Big-O: O(1)."""
        self.root = None

    def set(self, key: str, val: float):
        """
        Menyisipkan variabel baru atau memperbarui nilai jika key sudah ada.
        Algoritma berdasarkan TreeInsert (Goodrich, Code Fragment 11.3).
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n).
        """
        if self.root is None:
            self.root = VarBSTNode(key, val)
        else:
            self._subtree_set(self.root, key, val)

    def _subtree_set(self, p, key, val):
        """Helper rekursif untuk penyisipan node."""
        if key == p.key:
            p.val = val  # Update nilai jika key sudah ada [4]
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

    def get(self, key: str):
        """
        Mencari nilai variabel berdasarkan key.
        Algoritma berdasarkan TreeSearch (Goodrich, Code Fragment 11.2).
        Big-O Waktu: Rata-rata O(log n), Terburuk O(n).
        """
        node = self._subtree_search(self.root, key)
        if node is not None:
            return node.val
        return None

    def _subtree_search(self, p, key):
        """Helper rekursif untuk pencarian node [3, 6]."""
        if p is None:
            return None
        if key == p.key:
            return p
        elif key < p.key:
            return self._subtree_search(p.left, key)
        else:
            return self._subtree_search(p.right, key)

    def list_all(self):
        """
        Menghasilkan list (key, value) yang terurut alfabetis.
        Menggunakan Inorder Traversal (Goodrich, Code Fragment 8.15).
        Big-O Waktu: O(n) [7, 8].
        """
        result = []
        self._subtree_inorder(self.root, result)
        return result

    def _subtree_inorder(self, p, result):
        """Helper rekursif untuk traversal inorder [9]."""
        if p is not None:
            self._subtree_inorder(p.left, result)
            result.append((p.key, p.val)) # "Visit" action [7]
            self._subtree_inorder(p.right, result)

# ─── CONTOH PENGUJIAN (BIAR BISA DI RUN) ───
if __name__ == "__main__":
    bst = VarBST()
    
    # Skenario: SET a 3.14, SET b 2.0, SET c 5.5
    print("Menyimpan variabel...")
    bst.set("b", 2.0)
    bst.set("a", 3.14)
    bst.set("c", 5.5)
    
    # Uji GET
    print(f"Pencarian 'a': {bst.get('a')}") # Output: 3.14
    print(f"Pencarian 'z' (tidak ada): {bst.get('z')}") # Output: None
    
    # Uji LIST_ALL (Inorder)
    print("\nDaftar variabel terurut (Inorder):")
    for key, val in bst.list_all():
        print(f"{key} = {val}")