from src.data_structures.linked_list import Node

def test_linked_list():
    print("=== TEST LINKED LIST NODE ===")

    # Membuat node menggunakan kelas Node yang benar
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    # Menyambungkan node
    node1.next = node2
    node2.next = node3

    # Traversal linked list
    current = node1

    while current:
        print(current.data)
        current = current.next

# Jalankan test
test_linked_list()