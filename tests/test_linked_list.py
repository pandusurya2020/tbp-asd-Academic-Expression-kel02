import sys
import os
import pytest

# Trik Teknis: Menambahkan root folder proyek ke path agar folder 'src' terbaca
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mengimpor kelas dari file src/data_structures/linked_list.py
from src.data_structures.linked_list import SinglyLinkedList

def test_basic_ops():
    """Menguji operasi dasar dan kasus batas (boundary cases) [9]."""
    sll = SinglyLinkedList()
    
    # Test 1: Kondisi awal (Empty Sequence) [9]
    assert sll.is_empty() is True
    assert len(sll) == 0
    
    # Test 2: Menambah elemen (Add First) [1]
    sll.add_first("A")
    assert len(sll) == 1
    assert sll.get_first() == "A"
    
    # Test 3: Menambah beberapa elemen (LIFO behavior) [10]
    sll.add_first("B")
    assert sll.get_first() == "B"
    assert len(sll) == 2
    
    # Test 4: Penghapusan elemen (Remove First) [2]
    val = sll.remove_first()
    assert val == "B"
    assert len(sll) == 1
    assert sll.get_first() == "A"

def test_empty_exception():
    """Menguji apakah error ValueError muncul saat list kosong dihapus [2]."""
    sll = SinglyLinkedList()
    with pytest.raises(ValueError, match="empty"):
        sll.remove_first()

# Bagian ini membuat file tes bisa dijalankan langsung dengan 'python tests/test_linked_list.py'
if __name__ == "__main__":
    # Menjalankan pytest pada file ini sendiri secara otomatis [11]
    import pytest
    pytest.main([__file__, "-v", "-s"])