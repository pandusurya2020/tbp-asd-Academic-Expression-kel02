from typing import Any, Optional

class QueueLL:
    class _Node:
        """Kelas internal privat untuk merepresentasikan simpul (Node) Linked List."""
        def __init__(self, element: Any, next_node: Optional['QueueLL._Node'] = None):
            self.element: Any = element  # Menyimpan data/token
            self.next: Optional['QueueLL._Node'] = next_node   # Menunjuk ke simpul berikutnya

    def __init__(self):
        """Inisialisasi antrean kosong. Big-O: O(1)"""
        self._head: Optional[QueueLL._Node] = None  # Menunjuk ke elemen terdepan (tempat dequeue)
        self._tail: Optional[QueueLL._Node] = None  # Menunjuk ke elemen terakhir (tempat enqueue)
        self._size: int = 0     # Mencatat jumlah elemen dalam antrean

    def __len__(self) -> int:
        """Mengembalikan jumlah elemen di dalam antrean."""
        return self._size

    def is_empty(self) -> bool:
        """Mengembalikan True jika antrean dalam kondisi kosong."""
        return self._size == 0

    def first(self) -> Any:
        """Mengembalikan elemen terdepan tanpa menghapusnya. Big-O: O(1)"""
        if self.is_empty():
            raise IndexError("Queue Underflow: Antrean kosong!")
        return self._head.element

    def enqueue(self, e: Any) -> None:
        """Memasukkan elemen baru 'e' ke bagian belakang antrean (Tail). Big-O: O(1)"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            if self._tail is not None:
                self._tail.next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self) -> Any:
        """Mengeluarkan dan mengembalikan elemen terdepan dari antrean (Head). Big-O: O(1)"""
        if self.is_empty():
            raise IndexError("Queue Underflow: Antrean kosong!")
        
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        
        if self.is_empty():
            self._tail = None
            
        return answer

# =================================================================
# SAKLAR UJI COBA OTOMATIS UNTUK LAMPIRAN OUTPUT MAKALAH QUEUE
# =================================================================
if __name__ == "__main__":
    print("\n=== SAKLAR UJI COBA QUEUE LINKED LIST KELOMPOK 02 ===")
    
    # 1. Inisialisasi struktur antrean baru
    q = QueueLL()
    print(f"-> Apakah antrean awal kosong? {q.is_empty()}")
    
    # 2. Simulasi memasukkan token operasi matematika (Enqueue)
    print("\n-> Melakukan Enqueue 3 elemen secara berurutan (Token1, Token2, Token3)...")
    q.enqueue("Token1")
    q.enqueue("Token2")
    q.enqueue("Token3")
    print(f"   Ukuran antrean sekarang : {len(q)} elemen")
    print(f"   Elemen terdepan (First) : '{q.first()}' (Big-O: O(1))")
    
    # 3. Simulasi mengeluarkan token operasi matematika (Dequeue)
    print("\n-> Melakukan Operasi Dequeue 2 elemen terdepan...")
    print(f"   Hasil Dequeue ke-1 : '{q.dequeue()}'")
    print(f"   Hasil Dequeue ke-2 : '{q.dequeue()}'")
    
    # 4. Memeriksa status akhir antrean
    print(f"\n   Elemen terdepan sekarang : '{q.first()}'")
    print(f"   Ukuran antrean akhir     : {len(q)} elemen")
    print("=======================================================\n")