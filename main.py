"""
==========================================================
  TUGAS PEMROGRAMAN: DYNAMIC PROGRAMMING & GREEDY
==========================================================
  Mata Kuliah : Perancangan dan Analisa Algoritma
  Semester    : 6

  Program ini mengimplementasikan dan membandingkan:
  1. 0/1 Knapsack  -- Dynamic Programming
  2. Fractional Knapsack -- Greedy

  Jalankan: python main.py
==========================================================
"""

import sys

# Fix encoding untuk Windows terminal (cp1252 tidak support Unicode)
sys.stdout.reconfigure(encoding="utf-8")

from knapsack_dp import knapsack_01
from knapsack_greedy import fractional_knapsack
from visualizer import (
    print_header,
    display_items_table,
    display_dp_table,
    display_dp_backtrack,
    display_dp_result,
    display_sorted_items,
    display_greedy_steps,
    display_greedy_result,
    display_comparison,
    display_complexity_analysis,
)


# ============================================================
# DATA INPUT
# ============================================================
ITEMS = [
    {"name": "Laptop",     "weight": 4, "value": 10},
    {"name": "Buku Tebal", "weight": 4, "value": 12},
    {"name": "Headphone",  "weight": 2, "value": 5},
    {"name": "Charger",    "weight": 3, "value": 6},
    {"name": "Mouse",      "weight": 1, "value": 3},
    {"name": "Tablet",     "weight": 5, "value": 8},
]
CAPACITY = 10


def main():
    """Fungsi utama — menjalankan kedua algoritma dan menampilkan hasil."""

    # ===========================================================
    # PEMBUKA
    # ===========================================================
    print_header("TUGAS PEMROGRAMAN: DYNAMIC PROGRAMMING & GREEDY")
    print("  Mata Kuliah : Perancangan dan Analisa Algoritma")
    print("  Bahasa      : Python")
    print()
    print("  Algoritma yang diimplementasikan:")
    print("    1. 0/1 Knapsack        → Dynamic Programming (DP)")
    print("    2. Fractional Knapsack  → Greedy")
    print()

    # ===========================================================
    # DATA INPUT
    # ===========================================================
    display_items_table(ITEMS, CAPACITY, "DATA INPUT — Daftar Barang")

    # ===========================================================
    # ALGORITMA 1: DYNAMIC PROGRAMMING — 0/1 KNAPSACK
    # ===========================================================
    print_header("ALGORITMA 1: DYNAMIC PROGRAMMING — 0/1 KNAPSACK")
    print("  Studi Kasus:")
    print("  Mahasiswa memiliki tas dengan kapasitas 10 kg dan ingin")
    print("  memilih barang yang dimasukkan agar nilai total maksimum.")
    print("  Setiap barang hanya bisa diambil seluruhnya atau tidak")
    print("  sama sekali (tidak boleh dipecah).")
    print()

    # Jalankan algoritma
    dp_max_val, dp_selected, dp_table, dp_steps = knapsack_01(ITEMS, CAPACITY)

    # Visualisasi
    display_dp_table(ITEMS, dp_table, dp_selected, CAPACITY)
    display_dp_backtrack(ITEMS, dp_table, dp_selected, CAPACITY)
    display_dp_result(dp_max_val, dp_selected, CAPACITY)

    # ===========================================================
    # ALGORITMA 2: GREEDY — FRACTIONAL KNAPSACK
    # ===========================================================
    print_header("ALGORITMA 2: GREEDY — FRACTIONAL KNAPSACK")
    print("  Studi Kasus:")
    print("  Kurir memiliki tas kapasitas 10 kg dan boleh mengambil")
    print("  sebagian barang untuk memaksimalkan keuntungan. Setiap")
    print("  barang memiliki berat dan nilai, dan kurir boleh mengambil")
    print("  fraksi/sebagian dari suatu barang.")
    print()

    # Jalankan algoritma
    greedy_max_val, greedy_selected, greedy_steps, sorted_items = fractional_knapsack(
        ITEMS, CAPACITY
    )

    # Visualisasi
    display_sorted_items(sorted_items)
    display_greedy_steps(greedy_steps, CAPACITY)
    display_greedy_result(greedy_max_val, greedy_selected, CAPACITY)

    # ===========================================================
    # PERBANDINGAN & ANALISIS
    # ===========================================================
    display_comparison(
        dp_result=(dp_max_val, dp_selected),
        greedy_result=(greedy_max_val, greedy_selected),
        capacity=CAPACITY,
    )

    display_complexity_analysis(n=len(ITEMS), W=CAPACITY)

    # ===========================================================
    # PENUTUP
    # ===========================================================
    print_header("PROGRAM SELESAI")
    print("  Terima kasih telah menjalankan program ini.")
    print("  Semua visualisasi algoritma telah ditampilkan di atas.")
    print()


if __name__ == "__main__":
    main()
