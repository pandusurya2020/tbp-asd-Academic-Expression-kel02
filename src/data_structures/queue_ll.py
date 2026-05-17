class QueueLL:
    class _Node:
        """Kelas internal privat untuk merepresentasikan simpul (Node) Linked List."""
        def _init_(self, element, next_node=None):
            self.element = element  # Menyimpan data/token
            self.next = next_node   # Menunjuk ke simpul berikutnya

    def _init_(self):
        """Inisialisasi antrean kosong."""
        self._head = None  # Menunjuk ke elemen terdepan (tempat dequeue)
        self._tail = None  # Menunjuk ke elemen terakhir (tempat enqueue)
        self._size = 0     # Mencatat jumlah elemen dalam antrean

    def _len_(self):
        """Mengembalikan jumlah elemen di dalam antrean."""
        return self._size

    def is_empty(self):
        """Mengembalikan True jika antrean dalam kondisi kosong."""
        return self._size == 0

    def first(self):
        """Mengembalikan elemen terdepan tanpa menghapusnya."""
        # FIX: Cek None langsung pada _head agar Pylance tahu ini aman
        if self._head is None:
            raise IndexError("Queue Underflow: Antrean kosong!")
        return self._head.element

    def enqueue(self, e):
        """Memasukkan elemen baru 'e' ke bagian belakang antrean (Tail)."""
        newest = self._Node(e, None)
        # FIX: Cek None langsung pada _tail agar Pylance tahu _tail tidak None di bagian else
        if self._tail is None:
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Mengeluarkan dan mengembalikan elemen terdepan dari antrean (Head)."""
        # FIX: Cek None langsung pada _head
        if self._head is None:
            raise IndexError("Queue Underflow: Antrean kosong!")
        
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        
        if self._head is None:
            self._tail = None
            
        return answer