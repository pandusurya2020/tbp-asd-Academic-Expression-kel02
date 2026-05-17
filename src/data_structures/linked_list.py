from typing import Optional, Any # FIX: Tambahkan Any kapital di sini

class Node:
    """Simpul tunggal untuk Linked List dengan proteksi objek kosong."""
    def __init__(self, data: Any, next_node: Optional['Node'] = None): # FIX: any -> Any
        self.data: Any = data # FIX: any -> Any
        self.next: Optional['Node'] = next_node

class SinglyLinkedList:
    """Implementasi Singly Linked List sebagai fondasi Stack dan Queue."""
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def add_first(self, data: Any) -> None: # FIX: any -> Any
        new_node = Node(data, self._head)
        self._head = new_node
        if self.is_empty():
            self._tail = new_node
        self._size += 1

    def add_last(self, data: Any) -> None: # FIX: any -> Any
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            if self._tail is not None:
                self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def remove_first(self) -> Any: # FIX: any -> Any
        """Menghapus dan mengambil data dari barisan depan (Pop/Dequeue)."""
        if self._head is None:
            raise IndexError("Linked List kosong, tidak bisa menghapus elemen!")
        
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        
        if self.is_empty():
            self._tail = None
        return data

    def first(self) -> Any: # FIX: any -> Any
        """Melihat data di barisan paling depan tanpa menghapusnya (Top/Front)."""
        if self._head is None:
            raise IndexError("Linked List kosong, tidak ada elemen terdepan!")
        return self._head.data

    def last(self) -> Any: # FIX: any -> Any
        """Melihat data di barisan paling belakang (Tail)."""
        if self._tail is None:
            raise IndexError("Linked List kosong, tidak ada elemen terakhir!")
        return self._tail.data