# 🧮 Academic Expression Calculator (Kelompok 02)

**TBP Kelompok 02 - Algoritma dan Struktur Data (ELT60213)** *Program Studi S1 Teknik Elektro — Universitas Negeri Yogyakarta (2026)*

Aplikasi kalkulator akademik interaktif berbasis *CLI (Command Line Interface)* yang dirancang untuk mengurai, memvalidasi, dan mengevaluasi ekspresi matematika numerik serta simbolik. Proyek ini mengimplementasikan sinergi beberapa struktur data tingkat lanjut yang dibangun murni tanpa library bawaan untuk menjamin efisiensi performa asimtotik serta proteksi memori yang optimal.

---

## 👥 Anggota Kelompok & Pembagian Tugas

Sesuai dengan ketentuan proyek, setiap anggota bertanggung jawab atas modul spesifik yang diimplementasikan secara mandiri dari nol (*pure implementation*):

| Nama Anggota | NIM | Fokus Komponen / Modul Utama |
| :--- | :---: | :--- |
| **Pandu Surya Pratama** | 25051030005 | *Expression Tree* (Konstruksi & Visualisasi Hierarki Pohon) |
| **Gifara Hanifa Hermawan** | 25051030016 | *Stack*, Konversi Infix ke Postfix (*Shunting-Yard*), Evaluasi Postfix |
| **Ditha Bapra Nugraha Br Payung** | 25051030023 | *Queue*, Graph Dependensi Formula (*DAG Cycle Detection*) |
| **Nagita Calya** | 25051030030 | *Singly Linked List* (Fondasi Stack/Queue), Pembantu Evaluasi Postfix |
| **Dominicus Savio F. W. P.** | 25051030040 | *Binary Search Tree* (BST Tabel Variabel / *Symbol Table*) |

---

## 🚀 Fitur Utama Sistem

* **Expression Tree (Topik 5):** Menyusun token postfix menjadi pohon biner ekspresi secara dinamis, mengembalikan string infix dengan tanda kurung teratur lewat traversal inorder, serta melakukan evaluasi nilai secara rekursif.
* **BST Tabel Variabel (Symbol Table):** Menyimpan pasangan nama variabel dan nilai numeriknya (konstanta sains/matematika) menggunakan struktur pohon *Binary Search Tree* untuk pencarian cepat berbasis waktu logaritmik $O(\log n)$.
* **Graph Dependensi Formula (DAG):** Mendaftarkan keterkaitan antar-rumus ke dalam bentuk graf berarah tidak berputar (*Directed Acyclic Graph*) untuk mendeteksi siklus lingkaran setan (*infinite loops*) menggunakan metode penyortiran topologis.
* **Murni Tanpa Library Eksternal:** Seluruh struktur data fundamental (Node, Linked List, Stack, Queue, BST, Graph) diimplementasikan secara mandiri merujuk pada diktat kurikulum Goodrich & Tamassia.

---

## 🗂️ Struktur Direktori Proyek

```text
tbp-asd-Academic-Expression-kel02/
│
├── src/
│   ├── main.py                     # Pusat Komando Utama / Entry Point Aplikasi
│   │
│   ├── data_structures/            # Fondasi Struktur Data Murni (Low-Level)
│   │   ├── linked_list.py          # Singly Linked List & Representasi Node
│   │   ├── stack.py                # Implementasi ADT Stack
│   │   ├── bst.py                  # VarBST & VarBSTNode untuk Tabel Variabel
│   │   └── graph.py                # Graf berarah dengan Adjacency List
│   │
│   └── modules/                    # Implementasi Logika Bisnis Aplikasi (High-Level)
│       ├── cli_kalkulator.py       # Loop Antarmuka CLI & Simulasi Log Operasi
│       ├── konversi_infix_ke_postfix.py
│       ├── evaluasi_postfix.py
│       ├── expression_tree.py
│       └── graph_dependensi_formula.py
│
├── tests/                          # Berkas Unit Testing Komponen Proyek
│   ├── test_linked_list.py
│   ├── test_stack.py
│   ├── test_bst.py
│   └── test_graph.py
│
├── docs/                           # Dokumentasi Cetak & Laporan Resmi
│   ├── laporan_final_calculator.pdf
│   └── tren_runtime_linear.png     # Grafik Analisis Performa Eksperimen Bab V
│
├── requirements.txt                # Dependensi pustaka luar untuk Visualisasi (Matplotlib/Numpy)
└── README.md                       # Panduan Utama Proyek (Berkas Ini)

---

🛠️ Panduan Instalasi & Cara Menjalankan
Ikuti langkah-langkah di bawah ini untuk mengonfigurasi lingkungan kerja lokal dan mengeksekusi aplikasi kalkulator.
1. Prasyarat SistemPastikan perangkat Anda sudah terpasang interpreter Python versi 3.10 atau yang lebih baru. Periksa versi aktif Anda menggunakan terminal:Bashpython --version
2. Langkah Klone & Pembuatan Virtual EnvironmentUnduh repositori proyek dari GitHub kelompok ke direktori lokal Anda:Bashgit clone [https://github.com/username/tbp-asd-Academic-Expression-kel02.git](https://github.com/username/tbp-asd-Academic-Expression-kel02.git)
cd tbp-asd-Academic-Expression-kel02
Buat dan aktifkan lingkungan terisolasi (.venv) agar dependensi pustaka tidak mengganggu sistem global:Windows (PowerShell / CMD):Bashpython -m venv .venv
.venv\Scripts\activate
Linux / macOS:Bashpython -m venv .venv
source .venv/bin/activate
3. Instalasi Dependensi EksternalPasang pustaka pendukung grafik analisis laboratorium (matplotlib dan numpy) melalui perintah manajer paket pip:Bashpip install -r requirements.txt
4. Mengeksekusi Aplikasi UtamaJalankan pusat komando aplikasi utama kalkulator interaktif dengan mengetik perintah berikut di root folder:Bashpython src/main.py
5. Menjalankan Unit Testing & Eksperimen RuntimeUji Validasi Unit Struktur Data:Bashpython -m tests.test_linked_list
python -m tests.test_bst

---

Uji Beban Performa Analisis Kompleksitas (Benchmark):Bashpython experiments/benchmark.py
📊 Analisis Kompleksitas Real-Time
Setiap eksekusi komando pada antarmuka aplikasi ini akan secara otomatis menampilkan kalkulasi teoretis Big-O (seperti waktu pencarian simbol variabel dalam $O(\log n)$ atau visualisasi pohon dalam $O(n)$) untuk memberikan transparansi penuh terhadap efisiensi algoritma yang diimplementasikan.
