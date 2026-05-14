class FormulaDAG:
def __init__(self):
self.adj: Dict[str, List[str]] = {} # formula -> [depends_on]
self.formulas: Dict[str, str] = {} # nama -> ekspresi
def define(self, nama: str, ekspresi: str, deps: List[str]) -> None:
"""Tambahkan formula dan dependensinya."""
# TODO: deteksi siklus, tambahkan ke adj dan formulas
pass
def topological_sort(self) -> List[str]:
"""
Urutan evaluasi valid (DFS-based).
Big-O: O(V+E).
Raise ValueError jika ada siklus.
"""
# TODO: implementasikan Kahn's algorithm atau DFS topo sort
pass