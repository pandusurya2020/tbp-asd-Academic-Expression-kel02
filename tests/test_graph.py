import math
from typing import Optional, Dict, List, Tuple
import unittest

class FormulaDAG:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {} # formula -> [depends_on]
        self.formulas: Dict[str, str] = {} # nama -> ekspresi

    def define(self, nama: str, ekspresi: str, deps: List[str]) -> None:
        """Tambahkan formula dan dependensinya."""
        old_deps = self.adj.get(nama)
        old_expr = self.formulas.get(nama)

        self.adj[nama] = deps
        self.formulas[nama] = ekspresi

        try:
            self.topological_sort()  # akan raise jika ada siklus
        except ValueError:
            if old_deps is not None:
                self.adj[nama] = old_deps
                self.formulas[nama] = old_expr
            else:
                del self.adj[nama]
                del self.formulas[nama]
            raise

    def topological_sort(self) -> List[str]:
        all_nodes = set(self.adj.keys())
        for deps in self.adj.values():
            all_nodes.update(deps)

        indegree = {u: 0 for u in all_nodes}
        graph: Dict[str, List[str]] = {u: [] for u in all_nodes}

        for formula, deps in self.adj.items():
            for dep in deps:
                graph[dep].append(formula)
                indegree[formula] += 1

        queue = [u for u, deg in indegree.items() if deg == 0]
        result = []

        while queue:
            curr = queue.pop(0)
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(all_nodes):
            raise ValueError("Siklus ketergantungan terdeteksi")

        return result  


#KODE PENGUJIAN (UNITTEST)
class TestFormulaDAG(unittest.TestCase):
    def setUp(self):
        self.dag = FormulaDAG()

    def test_define_no_dependencies(self):
        self.dag.define("A", "10", [])
        self.assertIn("A", self.dag.formulas)
        self.assertEqual(self.dag.formulas["A"], "10")
        self.assertEqual(self.dag.adj["A"], [])
        self.assertEqual(self.dag.topological_sort(), ["A"])

    def test_linear_dependencies(self):
        self.dag.define("A", "B + 1", ["B"])
        self.dag.define("B", "C * 2", ["C"])
        order = self.dag.topological_sort()
        self.assertEqual(order, ["C", "B", "A"])

    def test_complex_dependencies(self):
        self.dag.define("Total", "Subtotal + Pajak", ["Subtotal", "Pajak"])
        self.dag.define("Pajak", "Subtotal * 0.1", ["Subtotal"])
        self.dag.define("Subtotal", "Harga * Qty", ["Harga", "Qty"])
        
        order = self.dag.topological_sort()
        self.assertTrue(order.index("Harga") < order.index("Subtotal"))
        self.assertTrue(order.index("Qty") < order.index("Subtotal"))
        self.assertTrue(order.index("Subtotal") < order.index("Pajak"))
        self.assertTrue(order.index("Subtotal") < order.index("Total"))
        self.assertTrue(order.index("Pajak") < order.index("Total"))

    def test_cycle_detection(self):
        self.dag.define("A", "B + 1", ["B"])
        with self.assertRaises(ValueError) as context:
            self.dag.define("B", "A * 2", ["A"])
        self.assertEqual(str(context.exception), "Siklus ketergantungan terdeteksi")

    def test_self_reference_cycle(self):
        with self.assertRaises(ValueError):
            self.dag.define("A", "A + 1", ["A"])

    def test_rollback_on_cycle_new_node(self):
        self.dag.define("A", "10", [])
        self.dag.define("B", "A + 5", ["A"])
        with self.assertRaises(ValueError):
            self.dag.define("A", "C * 2", ["C", "B"])
        self.assertEqual(self.dag.formulas["A"], "10")
        self.assertEqual(self.dag.adj["A"], [])

    def test_rollback_on_cycle_existing_node(self):
        self.dag.define("X", "100", [])
        self.dag.define("Y", "X * 2", ["X"])
        with self.assertRaises(ValueError):
            self.dag.define("X", "Y + 50", ["Y"])
        self.assertEqual(self.dag.formulas["X"], "100")
        self.assertEqual(self.dag.adj["X"], [])

if __name__ == '__main__':
    unittest.main()
