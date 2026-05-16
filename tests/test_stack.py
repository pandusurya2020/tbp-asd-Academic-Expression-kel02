import unittest
import sys
import os

# Sinkronisasi path agar folder 'src' bisa terdeteksi oleh folder 'tests'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def test_push_and_pop(self):
        """Menguji apakah fungsi push dan pop bekerja sesuai prinsip LIFO"""
        s = Stack()
        s.push("Data A")
        s.push("Data B")
        
        # Memastikan Data B yang keluar duluan karena posisi paling atas (LIFO)
        self.assertEqual(s.pop(), "Data B")
        # Memastikan Data A tersisa di tumpukan setelah Data B diambil
        self.assertEqual(s.peek(), "Data A")

    def test_is_empty(self):
        """Menguji apakah deteksi stack kosong berfungsi dengan benar"""
        s = Stack()
        self.assertTrue(s.is_empty())
        
        s.push("Data C")
        self.assertFalse(s.is_empty())

if __name__ == '__main__':
    unittest.main()