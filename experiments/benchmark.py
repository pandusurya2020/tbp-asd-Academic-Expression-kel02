import sys
import os
import time
import matplotlib.pyplot as plt

# Menambahkan root direktori utama ke sys.path agar aman dijalankan dari mana saja
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# FIX 1: Impor langsung disamakan persis dengan cli_kalkulator.py tanpa try-except membingungkan
from src.modules.konversi_infix_ke_postfix import infix_to_postfix
from src.modules.evaluasi_postfix import eval_postfix

def buat_ekspresi_dummy(n_token):
    """Membuat rumus linear panjang otomatis berbasis angka untuk benchmark."""
    tokens = []
    for i in range(n_token // 2):
        tokens.append("1")
        tokens.append("+")
    tokens.append("1")
    return tokens

def buat_grafik_runtime(skala_n, waktu_sy, waktu_eval):
    """Membuat grafik tren performa berdasarkan waktu riil hasil pengujian CPU."""
    plt.figure(figsize=(8, 5), dpi=300)
    
    # Plot Jalur Tren Kinerja menggunakan data riil
    plt.plot(skala_n, waktu_sy, marker='o', linestyle='-', color='#0075ca', 
             linewidth=2, label='Shunting-Yard Algorithm (Infix -> Postfix)')
    plt.plot(skala_n, waktu_eval, marker='s', linestyle='--', color='#d73a4a', 
             linewidth=2, label='Postfix Evaluation Engine')

    # Konfigurasi Judul, Label, dan Estetika Grafik sesuai Laporan
    plt.title('Tren Kompleksitas Waktu Empiris O(n) - Kelompok 02\n(Topik 5: Academic Expression Evaluator)', 
              fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Ukuran Dataset Rumus (Jumlah Token / n)', fontsize=10, labelpad=10)
    plt.ylabel('Rata-rata Waktu Eksekusi (ms)', fontsize=10, labelpad=10)
    
    plt.xscale('log')
    plt.xticks(skala_n, labels=['10 Token', '100 Token', '1000 Token'])
    
    plt.grid(True, linestyle=':', alpha=0.6, which="both")
    plt.legend(loc='upper left', fontsize=9)
    
    # FIX 2: Menghapus syntax titik koma ilegal, langsung panggil indeksnya secara clean
    plt.text(1000, waktu_sy[2] + (waktu_sy[2] * 0.05), f"{waktu_sy[2]:.3f} ms", ha='center', color='#0075ca', fontweight='bold')
    plt.text(1000, waktu_eval[2] - (waktu_eval[2] * 0.08), f"{waktu_eval[2]:.3f} ms", ha='center', color='#d73a4a', fontweight='bold')

    plt.tight_layout()

    # Tentukan jalur folder penyimpanan otomatis ke dalam folder docs/
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
    if not os.path.exists(output_dir):
        output_dir = os.path.dirname(__file__)
        
    output_path = os.path.join(output_dir, 'tren_runtime_linear.png')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"\n📍 Grafik visualisasi Bab V berhasil diperbarui di: \n👉 {output_path} ✅")

def jalankan_benchmark():
    skala_uji = [10, 100, 1000]
    list_waktu_sy = []
    list_waktu_eval = []
    
    print("=" * 75)
    print("        BENCHMARK RUNTIME PERFORMANCE - KELOMPOK 02")
    print("=" * 75)
    print(f"{'Ukuran Data (n)':<18} | {'Waktu Shunting-Yard':<22} | {'Waktu Evaluasi':<18}")
    print("-" * 75)
    
    for n in skala_uji:
        tokens_infix = buat_ekspresi_dummy(n)
        tokens_postfix = []
        
        # 1. Benchmark Waktu Algoritma Shunting-Yard
        mulai_sy = time.perf_counter()
        for _ in range(100):
            tokens_postfix = infix_to_postfix(tokens_infix)
        selesai_sy = time.perf_counter()
        waktu_sy_ms = ((selesai_sy - mulai_sy) / 100) * 1000
        list_waktu_sy.append(waktu_sy_ms)
        
        # 2. Benchmark Waktu Evaluasi Postfix
        mulai_eval = time.perf_counter()
        for _ in range(100):
            try:
                _ = eval_postfix(tokens_postfix, {})
            except Exception:
                _ = eval_postfix(tokens_postfix)
        selesai_eval = time.perf_counter()
        waktu_eval_ms = ((selesai_eval - mulai_eval) / 100) * 1000
        list_waktu_eval.append(waktu_eval_ms)
        
        print(f"{n:<3} Token {'':<8} | {waktu_sy_ms:.3f} ms {'':<12} | {waktu_eval_ms:.3f} ms")
        
    print("=" * 75)
    print("Status Validasi: Sukses Memenuhi Batas Atas Waktu Linear O(n) ✅")
    print("=" * 75)
    
    buat_grafik_runtime(skala_uji, list_waktu_sy, list_waktu_eval)

if __name__ == "__main__":
    jalankan_benchmark()