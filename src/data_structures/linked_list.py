from typing import Optional

class LLNode:
    """
    Node untuk Singly Linked List
    Digunakan oleh:
    - Stack
    - Queue
    - History
    """

    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None