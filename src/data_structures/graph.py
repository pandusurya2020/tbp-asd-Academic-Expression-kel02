from typing import Dict, List

class Graph:
    def __init__(self):
        # Menggunakan representasi Adjacency List (Daftar Keterkaitan)
        # Contoh struktur: { 'F1': ['F2', 'F3'], 'F2': ['F3', 'F4'] }
        self.adj_list: Dict[str, List[str]] = {}
        
    def tambah_simpul(self, v: str) -> None:
        """Menambahkan simpul (vertex/nama fungsi formula) baru ke dalam graf jika belum ada."""
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def tambah_sisi(self, u: str, v: str) -> None:
        """
        Menambahkan sisi terarah (directed edge) dari simpul u ke v (u -> v).
        Artinya: Variabel 'u' wajib dihitung terlebih dahulu sebelum rumus 'v' bisa dievaluasi.
        """
        self.tambah_simpul(u)
        self.tambah_simpul(v)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            
    def dapatkan_tetangga(self, v: str) -> List[str]:
        """Mengembalikan list simbol formula yang bergantung langsung pada simpul v."""
        return self.adj_list.get(v, [])
        
    def semua_simpul(self) -> List[str]:
        """Mengembalikan seluruh daftar simpul formula yang terdaftar di dalam graf."""
        return list(self.adj_list.keys())

    def memiliki_siklus(self) -> bool:
        """
        Mendeteksi siklus melingkar menggunakan algoritma pewarnaan DFS (Graph Coloring).
        Status warna: 0 = WHITE, 1 = GRAY, 2 = BLACK
        """
        status_warna = {v: 0 for v in self.adj_list}
        
        def dfs_kunjung(u: str) -> bool:
            status_warna[u] = 1 # Ubah status menjadi GRAY (sedang dikunjungi)
            
            for v in self.dapatkan_tetangga(u):
                # JIKA MENEMUI TETANGGA BERWARNA GRAY = TERBUKTI ADA SIKLUS MELINGKAR!
                if status_warna.get(v, 0) == 1:
                    return True
                # Jika tetangga masih WHITE, telusuri lebih dalam secara rekursif
                if status_warna.get(v, 0) == 0:
                    if dfs_kunjung(v):
                        return True
                        
            status_warna[u] = 2 # Ubah status menjadi BLACK (selesai aman)
            return False

        for simpul in list(self.adj_list.keys()):
            if status_warna[simpul] == 0:
                if dfs_kunjung(simpul):
                    return True
        return False

    def topological_sort(self) -> List[str]:
        """
        Mengurutkan rantai eksekusi rumus secara linier berbasis deret antrean (Topological Sort).
        Menggunakan Algoritma Kahn (In-Degree Elimination).
        """
        if self.memiliki_siklus():
            raise ValueError("Circular Dependency Detected: Rumus saling melingkar dan memicu deadlock!")
            
        # 1. Hitung Nilai In-Degree (jumlah panah masuk) untuk setiap simpul
        in_degree = {v: 0 for v in self.adj_list}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                in_degree[v] = in_degree.get(v, 0) + 1
                
        # 2. Masukkan semua simpul dengan In-Degree == 0 ke antrean awal
        queue = [v for v in self.adj_list if in_degree.get(v, 0) == 0]
        urutan_topologi = []
        
        # 3. Proses eliminasi simpul satu per satu
        while queue:
            u = queue.pop(0) # Ambil simpul terdepan
            urutan_topologi.append(u)
            
            for v in self.adj_list.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return urutan_topologi

# =================================================================
# SAKLAR UJI COBA OTOMATIS UNTUK LAMPIRAN OUTPUT MAKALAH
# =================================================================
if __name__ == "__main__":
    print("\n=== SAKLAR UJI COBA ALGORITMA KAHN & DFS GRAPH KELOMPOK 02 ===")
    
    g = Graph()
    # Membangun relasi dependensi berdasarkan contoh awalmu
    # Jika F1 butuh nilai A dan B, berarti A dan B harus jalan duluan (A -> F1, B -> F1)
    g.tambah_sisi("A", "F1")
    g.tambah_sisi("B", "F1")
    g.tambah_sisi("B", "F2")
    g.tambah_sisi("F1", "F3")
    
    print("-> Struktur Adjacency List Graf:")
    print(g.adj_list)
    
    print(f"\n-> Apakah ada hubungan rumus melingkar (Siklus)? {g.memiliki_siklus()}")
    
    try:
        urutan = g.topological_sort()
        print(f"-> Urutan Urutan Eksekusi Rumus yang Aman (Topological Sort):")
        print(f"   {' -> '.join(urutan)}")
    except ValueError as e:
        print(f"-> {e}")
        
    print("-" * 65)
    print("-> Simulasi Konflik: Menambahkan relasi melingkar (F3 menunjuk kembali ke A)")
    g.tambah_sisi("F3", "A")
    print(f"-> Apakah ada hubungan rumus melingkar (Siklus)? {g.memiliki_siklus()}")
    
    try:
        g.topological_sort()
    except ValueError as e:
        print(f"-> Hasil Pemicu Sistem: {e}")
    print("==============================================================\n")