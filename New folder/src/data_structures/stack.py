from typing import Optional, Any

class LLNode:
    """Simpul untuk menyimpan data dan pointer ke simpul berikutnya."""
    def __init__(self, data: Any = None):
        self.data: Any = data
        self.next: Optional['LLNode'] = None

class Stack:
    """Struktur data Tumpukan (LIFO) berbasis Singly Linked List."""
    def __init__(self):
        self.top: Optional[LLNode] = None
        self._size: int = 0

    def push(self, data: Any) -> None:
        """Menambahkan data baru ke tumpukan teratas. Kompleksitas: O(1)"""
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> Any:
        """Mengambil dan menghapus data teratas. Kompleksitas: O(1)"""
        if self.is_empty():
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self) -> Any:
        """Melihat data teratas tanpa menghapusnya. Kompleksitas: O(1)"""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self) -> bool:
        """Mengecek apakah tumpukan kosong."""
        return self._size == 0