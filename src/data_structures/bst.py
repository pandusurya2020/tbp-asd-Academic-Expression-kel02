class VarBSTNode:
    def __init__(self, key: str, val: float):
        self.key = key; self.val = val
        self.left = self.right = None
class VarBST:
    def __init__(self): self.root = None
    def set(self, key: str, val: float): pass # TODO
    def get(self, key: str) -> Optional[float]: pass # TODO
    def delete(self, key: str): pass # TODO
    def list_all(self) -> List[Tuple[str,float]]: pass # TODO inorder