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

## 🏛️ Arsitektur Sistem & Aliran Data

Aplikasi ini menggunakan *Arsitektur Aliran Data Modular* (Pipe-and-Filter Style). Setiap modul bekerja secara independen di mana hasil keluaran (output) suatu modul akan diteruskan langsung menjadi masukan (input) modul berikutnya melalui pipa aliran data sekuensial:

1. **Input & Tokenisasi (CLI Layer):** `cli_kalkulator.py` menerima input string ekspresi infix (misal: `a + b * 2`) dan memotongnya menjadi list token bersih berdasarkan spasi.
2. **Kompilasi Notasi (Logics Layer):** Modul `konversi_infix_ke_postfix.py` mengubah list token infix menjadi antrean token postfix menggunakan *Algoritma Shunting-Yard* bantuan Stack.
3. **Validasi Keterkaitan (Structure Layer):** Modul `graph_dependensi_formula.py` mendaftarkan rumus ke dalam *DAG (Directed Acyclic Graph)* untuk melakukan deteksi siklus (*cycle detection*) guna mencegah *infinite evaluation loops*.
4. **Pencarian Simbol (Storage Layer):** Jika token berupa huruf/variabel, `evaluasi_postfix.py` melakukan kueri pencarian nilai aktual secara logaritmik ke dalam pohon *BST (Binary Search Tree)* milik `bst_tabel_variabel.py`.
5. **Konstruksi Pohon & Output:** `expression_tree.py` menyusun token postfix menjadi struktur *Binary Tree* matematika untuk visualisasi hierarki operasi, lalu hasil final kalkulasi dicetak ke layar monitor pengguna.

---

## 📂 Struktur Direktori Proyek

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

## 🛠️ Panduan Instalasi (Installation Guide)
Ikuti langkah-langkah teknis di bawah ini untuk mempersiapkan lingkungan kerja lokal (environment) pada perangkat Anda sebelum menjalankan aplikasi:
*1. Kloning Repositori Proyek*
Buka terminal (Git Bash, CMD, atau PowerShell) di komputer Anda, lalu unduh repositori kelompok dari GitHub dengan perintah:
    git clone [https://github.com/username/tbp-asd-Academic-Expression-kel02.git](https://github.com/username/tbp-asd-Academic-Expression-kel02.git)
    cd tbp-asd-Academic-Expression-kel02
*2. Membuat & Mengaktifkan Lingkungan Virtual (.venv)*
Langkah ini wajib dilakukan agar paket pustaka eksternal proyek terisolasi dengan aman dan tidak merusak library Python global di sistem operasi Anda.
- Windows (PowerShell / CMD):
    python -m venv .venv
    .venv\Scripts\activate
- Linux / macOS:
    python -m venv .venv
    source .venv/bin/activate 
*3. Memasang Dependensi Pustaka (Requirements)*
Pasang pustaka pihak ketiga pendukung visualisasi grafik eksperimen runtime yang terdaftar di dalam berkas dependensi:
    pip install -r requirements.txt
  
---
  
## 💻 Cara Memakai Aplikasi (Usage Guide)
Aplikasi kalkulator ini bekerja secara interaktif melalui baris perintah terminal. Berikut adalah panduan cara mengaktifkan dan mengoperasikannya:
*1. Menjalankan Aplikasi Utama*
Pastikan posisi terminal Anda saat ini berada di folder utama (tbp-asd-Academic-Expression-kel02), lalu panggil gerbang utama aplikasi menggunakan perintah:
    Bashpython src/main.py
*2. Panduan Komando Interaktif CLI Kalkulator*
Setelah aplikasi berhasil menyala, terminal akan menampilkan prompt interaktif bertanda >> . Anda dapat mengetikkan perintah-perintah operasional berikut:
- Mendefinisikan Nilai Variabel (SET)
Digunakan untuk menyimpan variabel matematika ke dalam memori Tabel Simbol berbasis Binary Search Tree (BST).
    - Format: SET [nama_variabel] = [angka]
    - Contoh:
        >> SET x = 10
        >> SET y = 5
- Memanggil Nilai Variabel (GET)
Digunakan untuk memeriksa nilai aktual suatu variabel yang tersimpan di dalam struktur pohon BST secara logaritmik O(\log n).
    - Format: GET [nama_variabel]
    - Contoh:
        >> GET x
        Nilai x = 10.0
- Mengevaluasi Ekspresi Matematika (Kalkulator)
Ketik langsung rumus matematika yang ingin dihitung. Pastikan Anda memberikan spasi di setiap karakter/token ekspresi agar mesin parser dapat memotong string dengan benar.
    - Contoh Input: ```text
        ( x + y ) * 2
    - Alur Sistem: Mengonversi infix ke postfix (via Stack), mendeteksi siklus rumus (via Graph), menyusun Expression Tree, dan menghitung hasil final.
    - Contoh Output:
        Hasil Evaluasi: 30.0
- Melihat Semua Variabel Terdaftar (LIST)
Menampilkan seluruh daftar konstanta atau variabel yang sedang aktif di memori secara berurutan alfabetis menggunakan traversal pohon Inorder.
    - Contoh:
        >> LIST
- Keluar dari Program (KELUAR)
Digunakan untuk menghentikan loop aplikasi secara aman dan kembali ke terminal Windows normal.
    - Contoh:
        >> KELUAR
        Aplikasi dihentikan oleh pengguna. Sampai jumpa!
  
---
  
📊 Analisis Kompleksitas Real-Time
Setiap eksekusi komando pada antarmuka aplikasi ini akan secara otomatis menampilkan kalkulasi teoretis Big-O (seperti waktu pencarian simbol variabel dalam $O(\log n)$ atau visualisasi pohon dalam $O(n)$) untuk memberikan transparansi penuh terhadap efisiensi algoritma yang diimplementasikan.
    ### 🚀 Kirim Hasil Akhirnya ke GitHub

    Setelah file disimpan (**Ctrl + S**), kamu bisa langsung mengunggah pembaruan dokumen terlengkap ini ke repositori utama dengan mengetik tiga perintah berurutan di terminal:

    ```bash
    git add README.md
    git commit -m "update final readme md gabungan arsitektur dan panduan running"
    git push origin main