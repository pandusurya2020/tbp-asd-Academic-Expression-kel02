class FormulaDAG:
    def __init__(self):
        # self.adj: Map yang memetakan prerequisite ke daftar formula yang membutuhkannya
        # A -> B artinya A harus dievaluasi sebelum B (B tergantung pada A)
        self.adj = {} 
        self.formulas = {}   # nama_formula -> ekspresi_string
        self._all_nodes = set() # Menyimpan semua node unik

    def define(self, nama: str, ekspresi: str, deps: list):
        """
        Menambahkan formula baru dan relasi dependensinya.
        Big-O: O(1) amortized per penambahan edge [3].
        """
        self.formulas[nama] = ekspresi
        self._all_nodes.add(nama)
        
        if nama not in self.adj:
            self.adj[nama] = []
        
        # Jika formula 'nama' bergantung pada daftar 'deps'
        # Maka buat edge: dep -> nama (dep diproses duluan)
        for dep in deps:
            self._all_nodes.add(dep)
            if dep not in self.adj:
                self.adj[dep] = []
            self.adj[dep].append(nama)

    def topological_sort(self) -> list:
        """
        Mengembalikan list urutan evaluasi menggunakan algoritma Kahn.
        Mendeteksi siklus jika hasil tidak mencakup semua node.
        Big-O: O(V + E) [2, 4].
        """
        topo = []      # List hasil urutan
        incount = {node: 0 for node in self._all_nodes} # Map in-degree [5]

        # 1. Hitung in-degree (jumlah hambatan/prasyarat) tiap node
        for u in self.adj:
            for v in self.adj[u]:
                incount[v] += 1

        # 2. Masukkan semua node dengan in-degree 0 ke 'ready' list [1]
        # Node in-degree 0 adalah node yang tidak punya prasyarat (siap dihitung)
        ready = [node for node in self._all_nodes if incount[node] == 0]

        # 3. Proses 'ready' list (Kahn's Algorithm)
        while len(ready) > 0:
            u = ready.pop()    # Ambil formula yang tidak punya prasyarat lagi
            topo.append(u)
            
            for v in self.adj[u]: 
                incount[v] -= 1 # Satu prasyarat (u) sudah selesai
                if incount[v] == 0:
                    ready.append(v)

        # 4. Deteksi Siklus (Circular Dependency) [6, 7]
        if len(topo) < len(self._all_nodes):
            raise ValueError("Siklus terdeteksi! Formula tidak valid (Circular Dependency).")
            
        return topo

# ─── CONTOH PENGUJIAN (BIAR BISA DI RUN) ───
def test_graph():
    dag = FormulaDAG()
    try:
        # Contoh kasus pada Pertanyaan Analisis 5 [7]
        # F1 = a + b
        # F2 = F1 * c
        # F3 = F2 / F1
        dag.define("F1", "a + b", [])
        dag.define("F2", "F1 * c", ["F1"])
        dag.define("F3", "F2 / F1", ["F1", "F2"])
        
        print("Mencoba melakukan Topological Sort...")
        urutan = dag.topological_sort()
        print("Urutan Evaluasi yang Valid:", urutan)
        # Hasil yang diharapkan: ['F1', 'F2', 'F3'] (atau urutan logis lainnya)

        # Uji Deteksi Siklus
        print("\nMenambahkan dependensi melingkar: F1 bergantung pada F3...")
        dag.define("F1", "F3 + 1", ["F3"]) # Membuat siklus F1 -> F2 -> F3 -> F1
        dag.topological_sort()

    except ValueError as e:
        print(f"Error Terdeteksi: {e}")

if __name__ == "__main__":
    test_graph()