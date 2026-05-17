# Academic Expression Calculator (Kelompok 02)

Aplikasi kalkulator akademik interaktif berbasis *CLI (Command Line Interface)* yang dirancang untuk mengurai, memvalidasi, dan mengevaluasi ekspresi matematika numerik serta simbolik. Proyek ini mengimplementasikan sinergi beberapa struktur data tingkat lanjut untuk menjamin efisiensi performa asimtotik ($O(n)$ dan $O(1)$) serta proteksi memori yang optimal.

Proyek ini disusun untuk memenuhi Tugas Besar mata kuliah *Struktur Data dan Algoritma, Program Studi **Teknik Elektro, Fakultas Teknik, **Universitas Negeri Yogyakarta (2026)*.

---

## 👥 Anggota Kelompok 02 & Kontribusi Modul

| Nama Anggota | NIM | Fokus Komponen / Modul |
| :--- | :---: | :--- |
| *Pandu Surya Pratama* | 25051030005| g |
| *Gifara Hanifa Hermawan * | 25051030016| gg |
| *Ditha Bapra Nugraha Br Payung* | 25051030023| ggg |
| *Nagita Calya* | 25051030030| ggg |
| *Dominicus Savio F. W. P.* | 25051030040| gggn |


---

## 🏛️ Arsitektur Sistem & Aliran Data

Aplikasi ini menggunakan *Arsitektur Aliran Data Modular* (Pipe-and-Filter Style). Setiap modul bekerja secara independen di mana hasil keluaran (output) suatu modul akan diteruskan langsung menjadi masukan (input) modul berikutnya melalui pipa aliran data sekuensial:

1. *Input & Tokenisasi (CLI Layer):* cli_kalkulator.py menerima input string ekspresi infix (misal: a + b * 2) dan memotongnya menjadi list token bersih berdasarkan spasi.
2. *Kompilasi Notasi (Logics Layer):* Modul konversi_infix_ke_postfix.py mengubah list token infix menjadi antrean token postfix menggunakan *Algoritma Shunting-Yard* bantuan Stack.
3. *Validasi Keterkaitan (Structure Layer):* Modul graph_dependensi_formula.py mendaftarkan rumus ke dalam *DAG (Directed Acyclic Graph)* untuk melakukan deteksi siklus (cycle detection) via DFS pewarnaan guna mencegah infinite evaluation loops.
4. *Pencarian Simbol (Storage Layer):* Jika token berupa huruf/variabel, evaluasi_postfix.py melakukan kueri pencarian nilai aktual secara logaritmik ke dalam pohon *BST (Binary Search Tree)* milik bst_tabel_variabel.py.
5. *Konstruksi Pohon & Output:* expression_tree.py menyusun token postfix menjadi struktur *Binary Tree* matematika untuk visualisasi hierarki operasi, lalu hasil final kalkulasi dicetak ke layar monitor pengguna.

---

## 📂 Struktur Direktori Proyek