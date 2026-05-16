from typing import Any, Optional

class LLNode:
    """Wadah Simpul (Node) untuk menyimpan data dan pointer ke node selanjutnya."""
    def __init__(self, data: Any = None):
        self.data: Any = data
        self.next: Optional['LLNode'] = None

class Stack:
    """Struktur data Tumpukan (LIFO) berbasis Singly Linked List."""
    def __init__(self):
        self.top: Optional[LLNode] = None
        self._size: int = 0

    def push(self, data: Any) -> None:
        """Menambahkan data baru ke tumpukan teratas (O(1))."""
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> Any:
        """Mengambil dan menghapus data teratas (O(1))."""
        # Ganti dari 'if self.is_empty():' menjadi langsung cek None
        if self.top is None:
            return None
        
        # Sekarang Pylance tahu pasti self.top di bawah ini TIDAK None (Aman)
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self) -> Any:
        """Mengintip data teratas tanpa menghapusnya (O(1))."""
        # Ganti dari 'if self.is_empty():' menjadi langsung cek None
        if self.top is None:
            return None
            
        return self.top.data

    def is_empty(self) -> bool:
        """Memeriksa apakah tumpukan kosong."""
        return self._size == 0

    def __len__(self) -> int:
        """Mengembalikan jumlah elemen di dalam stack."""
        return self._size

# =======================================================
# KODE DI BAWAH INI UNTUK MENJALANKAN STACK SECARA MANDIRI
# =======================================================
if __name__ == "__main__":
    print("=== UJI COBA MANDIRI STRUKTUR DATA STACK ===")
    tumpukan = Stack()
    print(f"Apakah tumpukan kosong? {tumpukan.is_empty()}") 
    
    print("\n-> Memasukkan data: 'Buku A', 'Buku B', 'Buku C'")
    tumpukan.push("Buku A")
    tumpukan.push("Buku B")
    tumpukan.push("Buku C")
    
    print(f"Buku paling atas (Peek): {tumpukan.peek()}") 
    
    print("\n-> Mengambil data teratas (Pop):")
    print(f"Diambil: {tumpukan.pop()}") 
    print(f"Diambil: {tumpukan.pop()}") 
    
    print(f"\nBuku paling atas sekarang: {tumpukan.peek()}") 
    print(f"Apakah tumpukan kosong? {tumpukan.is_empty()}") 
    print("============================================")