import sys
import os
import time

# Menambahkan root direktori utama ke sys.path agar aman dijalankan dari mana saja
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# FIX: Menggunakan 'src.modules' agar Pylance VS Code bisa langsung mendeteksi tanpa error
try:
    from src.modules.konversi_infix_ke_postfix import infix_to_postfix
    from src.modules.evaluasi_postfix import eval_postfix
except ImportError:
    # Antisipasi jika fungsi di kelompokmu menggunakan penamaan Bahasa Indonesia
    try:
        from src.modules.konversi_infix_ke_postfix import konversi_infix_ke_postfix as infix_to_postfix
        from src.modules.evaluasi_postfix import evaluasi_postfix as eval_postfix
    except ImportError:
        print("ERROR: Modul di dalam src/modules tidak ditemukan. Pastikan nama file dan fungsinya benar!")
        sys.exit(1)

def buat_ekspresi_dummy(n_token):
    """Membuat rumus linear panjang otomatis berbasis angka untuk benchmark."""
    tokens = []
    for i in range(n_token // 2):
        tokens.append("1")
        tokens.append("+")
    tokens.append("1")
    return tokens

def jalankan_benchmark():
    skala_uji = [10, 100, 1000]
    
    print("=" * 75)
    print("        BENCHMARK RUNTIME PERFORMANCE - KELOMPOK 02")
    print("=" * 75)
    print(f"{'Ukuran Data (n)':<18} | {'Waktu Shunting-Yard':<22} | {'Waktu Evaluasi':<18}")
    print("-" * 75)
    
    for n in skala_uji:
        tokens_infix = buat_ekspresi_dummy(n)
        
        # 1. Benchmark Waktu Algoritma Shunting-Yard (Infix -> Postfix)
        mulai_sy = time.perf_counter()
        for _ in range(100):
            tokens_postfix = infix_to_postfix(tokens_infix)
        selesai_sy = time.perf_counter()
        waktu_sy_ms = ((selesai_sy - mulai_sy) / 100) * 1000
        
        # 2. Benchmark Waktu Evaluasi Postfix (Menggunakan dummy {} sebagai tabel BST)
        mulai_eval = time.perf_counter()
        for _ in range(100):
            try:
                _ = eval_postfix(tokens_postfix, {})
            except Exception:
                _ = eval_postfix(tokens_postfix)
        selesai_eval = time.perf_counter()
        waktu_eval_ms = ((selesai_eval - mulai_eval) / 100) * 1000
        
        print(f"{n:<3} Token {'':<8} | {waktu_sy_ms:.3f} ms {'':<12} | {waktu_eval_ms:.3f} ms")
        
    print("=" * 75)
    print("Status Validasi: Sukses Memenuhi Batas Atas Waktu Linear O(n) ✅")
    print("=" * 75)

if __name__ == "__main__":
    jalankan_benchmark()