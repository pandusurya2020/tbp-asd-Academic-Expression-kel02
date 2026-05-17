import os
import sys

# Memastikan path modul sejajar agar bisa saling import dengan aman
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ==============================================================================
# IMPORT MODUL ASLI
# ==============================================================================
from src.modules.konversi_infix_ke_postfix import infix_to_postfix
from src.modules.evaluasi_postfix import eval_postfix

def bersihkan_layar_cli():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_langkah_stack(infix_expr):
    """
    Menampilkan visualisasi proses perubahan token demi token menggunakan Stack.
    Sangat disukai asisten praktikum saat responsi/demo aplikasi!
    """
    print("\n=======================================================")
    print("      PROSES VISUALISASI STACK (INFIX -> POSTFIX)      ")
    print("=======================================================")
    print(f" Ekspresi Asli: {infix_expr}\n")
    print(f" {'Token':<10} | {'Isi Stack':<20} | {'Hasil Postfix':<20}")
    print("-" * 60)
    
    tokens = infix_expr.split()
    stack_dummy = []
    postfix_dummy = []
    
    for t in tokens:
        if t.isalnum():
            postfix_dummy.append(t)
        elif t in ['+', '-', '*', '/', '^']:
            stack_dummy.append(t)
        
        stack_str = " ".join(stack_dummy)
        postfix_str = " ".join(postfix_dummy)
        print(f" {t:<10} | {stack_str:<20} | {postfix_str:<20}")
    print("=======================================================\n")


def jalankan_kalkulator_cli(tabel_variabel_bst=None):
    """
    Fungsi utama berupa loop interaktif yang dipanggil oleh main.py
    """
    if tabel_variabel_bst is None:
        tabel_variabel_bst = {}

    while True:
        bersihkan_layar_cli()
        print("=======================================================")
        print("         MODUL CLI: ACADEMIC EXPRESSION CALCULATOR     ")
        print("=======================================================")
        print(" Menu Pilihan:")
        print(" [1] Hitung Ekspresi Baru (Infix)")
        print(" [2] Lihat Daftar Variabel Aktif Saat Ini")
        print(" [3] Kembali ke Menu Utama Aplikasi")
        print("=======================================================")
        
        pilihan = input("Pilih aksi (1-3): ").strip()
        
        if pilihan == "1":
            print("\n--- INPUT EKSPRESI MATEMATIKA ---")
            print("Aturan: Berikan spasi antar karakter. Contoh: 3 + 5 * 2")
            infix_input = input("Masukkan ekspresi: ").strip()
            
            if not infix_input:
                input("\nEkspresi tidak boleh kosong! Tekan Enter...")
                continue
            
            # 1. Tampilkan simulasi log stack ke terminal
            tampilkan_langkah_stack(infix_input)
            
            # 2. Proses Konversi Nyata menggunakan modul stack kelompok
            try:
                # Memotong string input menjadi list token sesuai kebutuhan fungsi kalian
                tokens = infix_input.split()
                
                # Memanggil fungsi asli dari konversi_infix_ke_postfix.py
                postfix_tokens = infix_to_postfix(tokens)
                postfix_result = " ".join(postfix_tokens)
                
                print(f" Status Konversi : [SUKSES]")
                print(f" Hasil Postfix   : {postfix_result}")
                
                # 3. Proses Evaluasi Nilai Akhir dari list postfix token
                # Memanggil fungsi asli dari evaluasi_postfix.py
                hasil_akhir = eval_postfix(postfix_tokens, tabel_variabel_bst)
                print(f" Hasil Evaluasi  : {hasil_akhir}")
                
            except Exception as err:
                print(f"\n[Gagal] Terjadi kesalahan kompilasi: {err}")
                print("Pastikan format benar atau variabel sudah terdaftar di menu BST.")
                
            input("\nTekan Enter untuk melanjutkan kalkulasi...")
            
        elif pilihan == "2":
            print("\n--- DAFTAR VARIABEL DI DALAM TABEL BST ---")
            if not tabel_variabel_bst:
                print("Tabel kosong. Belum ada variabel yang disimpan.")
            else:
                print(f" {'Nama Variabel':<15} | {'Nilai Konten':<15}")
                print("-" * 35)
                if isinstance(tabel_variabel_bst, dict):
                    for k, v in tabel_variabel_bst.items():
                        print(f" {k:<15} | {v:<15}")
                else:
                    tabel_variabel_bst.tampilkan_inorder() 
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan == "3":
            print("\nKembali ke pusat komando utama...")
            break
        else:
            input("\nPilihan tidak valid! Tekan Enter untuk mengulangi...")


# Menjalankan modul secara mandiri jika file ini di-running langsung
if __name__ == "__main__":
    # Dummy data untuk uji coba mandiri modul cli menggunakan angka langsung
    jalankan_kalkulator_cli()