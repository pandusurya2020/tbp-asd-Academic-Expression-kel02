from src.data_structures.linked_list import LLNode


def test_linked_list():

    print("=== TEST LINKED LIST NODE ===")

    # Membuat node
    node1 = LLNode(10)
    node2 = LLNode(20)
    node3 = LLNode(30)

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