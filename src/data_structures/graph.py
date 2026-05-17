class Graph:
    def __init__(self):
        # Menggunakan representasi Adjacency List (Daftar Keterkaitan)
        # Contoh struktur: { 'F1': ['F2', 'F3'], 'F2': ['F3', 'F4'] }
        self.adj_list = {}
        
    def tambah_simpul(self, v):
        """Menambahkan simpul (vertex/nama fungsi formula) baru ke dalam graf jika belum ada."""
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def tambah_sisi(self, u, v):
        """
        Menambahkan sisi terarah (directed edge) dari simpul u ke v (u -> v).
        Artinya: Variabel 'u' wajib dihitung terlebih dahulu sebelum rumus 'v' bisa dievaluasi.
        """
        self.tambah_simpul(u)
        self.tambah_simpul(v)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            
    def dapatkan_tetangga(self, v):
        """Mengembalikan list simbol formula yang bergantung langsung pada simpul v."""
        return self.adj_list.get(v, [])
        
    def semua_simpul(self):
        """Mengembalikan seluruh daftar simpul formula yang terdaftar di dalam graf."""
        return list(self.adj_list.keys())

    def memiliki_siklus(self):
        """
        Mendeteksi siklus melingkar menggunakan algoritma pewarnaan DFS (Graph Coloring).
        Status warna:
        0 = WHITE (Belum diperiksa)
        1 = GRAY  (Sedang diperiksa di call stack aktif / mendeteksi back-edge)
        2 = BLACK (Selesai diperiksa dan dinyatakan aman)
        """
        status_warna = {v: 0 for v in self.adj_list}
        
        def dfs_kunjung(u):
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

        # Melakukan perulangan untuk semua simpul demi mengantisipasi graf yang terputus
        for simpul in list(self.adj_list.keys()):
            if status_warna[simpul] == 0:
                if dfs_kunjung(simpul):
                    return True
        return False

    def topological_sort(self):
        """
        Mengurutkan rantai eksekusi rumus secara linier berbasis deret antrean (Topological Sort).
        Menggunakan Algoritma Kahn (In-Degree Elimination) sesuai standar uji asisten praktikum.
        """
        if self.memiliki_siklus():
            raise ValueError("Circular Dependency Detected: Rumus saling melingkar dan memicu deadlock!")
            
        # 1. Hitung Nilai In-Degree (jumlah panah masuk) untuk setiap simpul
        in_degree = {v: 0 for v in self.adj_list}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                in_degree[v] = in_degree.get(v, 0) + 1
                
        # 2. Masukkan semua simpul yang tidak punya hambatan masuk (In-Degree == 0) ke antrean
        queue = [v for v in self.adj_list if in_degree[v] == 0]
        urutan_topologi = []
        
        # 3. Proses eliminasi simpul satu per satu
        while queue:
            u = queue.pop(0) # Ambil simpul terdepan
            urutan_topologi.append(u)
            
            # Kurangi beban in-degree dari simpul tetangga yang terhubung
            for v in self.adj_list.get(u, []):
                in_degree[v] -= 1
                # Jika tetangga kini bebas hambatan (in-degree menjadi 0), masukkan ke antrean
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return urutan_topologi