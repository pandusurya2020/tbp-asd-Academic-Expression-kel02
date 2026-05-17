class QueueLL:
    class _Node:
        """Kelas internal privat untuk merepresentasikan simpul (Node) Linked List."""
        # FIX: Gunakan double underscore __init__
        def __init__(self, element, next_node=None):
            self.element = element  # Menyimpan data/token
            self.next = next_node   # Menunjuk ke simpul berikutnya

    # FIX: Gunakan double underscore __init__
    def __init__(self):
        """Inisialisasi antrean kosong."""
        self._head = None  # Menunjuk ke elemen terdepan (tempat dequeue)
        self._tail = None  # Menunjuk ke elemen terakhir (tempat enqueue)
        self._size = 0     # Mencatat jumlah elemen dalam antrean

    # FIX: Gunakan double underscore __len__
    def __len__(self):
        """Mengembalikan jumlah elemen di dalam antrean."""
        return self._size

    def is_empty(self):
        """Mengembalikan True jika antrean dalam kondisi kosong."""
        return self._size == 0

    def first(self):
        """Mengembalikan elemen terdepan tanpa menghapusnya."""
        if self._head is None:
            raise IndexError("Queue Underflow: Antrean kosong!")
        return self._head.element

    def enqueue(self, e):
        """Memasukkan elemen baru 'e' ke bagian belakang antrean (Tail)."""
        newest = self._Node(e, None)
        if self._tail is None:
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Mengeluarkan dan mengembalikan elemen terdepan dari antrean (Head)."""
        if self._head is None:
            raise IndexError("Queue Underflow: Antrean kosong!")
        
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        
        if self._head is None:
            self._tail = None
            
        return answer