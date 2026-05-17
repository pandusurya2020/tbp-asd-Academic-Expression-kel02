class LLNode:
    """Kelas ringan untuk menyimpan simpul (node) singly linked list.
    Referensi: Goodrich dkk. (Code Fragment 7.4).
    """
    # Menggunakan __slots__ untuk menghemat memori pada banyak instance node
    __slots__ = 'data', 'next' 

    def __init__(self, data=None, next_node=None):
        self.data = data      # Referensi ke objek pengguna [4]
        self.next = next_node # Referensi ke node selanjutnya

class SinglyLinkedList:
    """Implementasi murni Singly Linked List dari nol.
    Wajib digunakan sebagai fondasi Stack dan Queue pada proyek.
    """

    def __init__(self):
        """Membuat linked list kosong. Big-O: O(1)."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Mengembalikan jumlah elemen dalam list. Big-O: O(1). [3]"""
        return self._size

    def is_empty(self):
        """Mengembalikan True jika list kosong. Big-O: O(1). [3]"""
        return self._size == 0

    def add_first(self, e):
        """Menambahkan elemen e ke bagian depan list. Big-O: O(1). [3, 5]"""
        # Buat node baru, arahkan next ke head lama, lalu update head [6]
        self._head = LLNode(e, self._head)
        self._size += 1

    def remove_first(self):
        """Menghapus dan mengembalikan elemen pertama (head). Big-O: O(1). [3, 7]"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        answer = self._head.data
        self._head = self._head.next # Geser head ke node selanjutnya [8]
        self._size -= 1
        return answer

    def get_first(self):
        """Melihat elemen pertama tanpa menghapusnya. Big-O: O(1)."""
        if self.is_empty():
            return None
        return self._head.data

    def display(self):
        """Menampilkan semua elemen list untuk debugging. Big-O: O(n)."""
        elements = []
        curr = self._head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty List")

# ─── BAGIAN TEST (BIAR BISA LANGSUNG DI RUN) ───
if __name__ == '__main__':
    print("=== Menguji Singly Linked List ===")
    sll = SinglyLinkedList()
    
    print(f"Apakah kosong? {sll.is_empty()}") # True
    
    print("Menambah 'C', 'B', 'A' di depan...")
    sll.add_first('C')
    sll.add_first('B')
    sll.add_first('A')
    
    sll.display() # Output: A -> B -> C
    print(f"Ukuran list: {len(sll)}") # 3
    
    print(f"Hapus elemen pertama: {sll.remove_first()}") # A
    sll.display() # Output: B -> C
    
    print(f"Elemen depan sekarang: {sll.get_first()}") # B