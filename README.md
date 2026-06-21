# Tugas Pemrograman: Dynamic Programming & Greedy

## Mata Kuliah
Perancangan dan Analisa Algoritma — Semester 6

## Anggota Kelompok
| No | Nama | NIM |
|----|------|-----|
| 1  | ...  | ... |
| 2  | ...  | ... |
| 3  | ...  | ... |

## Deskripsi Tugas
Implementasi dua algoritma berbasis paradigma pemrograman yang berbeda:

### Algoritma 1: Dynamic Programming — 0/1 Knapsack
**Studi Kasus:** Mahasiswa memiliki tas dengan kapasitas 10 kg dan ingin memilih barang yang dimasukkan agar nilai total maksimum. Setiap barang hanya bisa diambil seluruhnya atau tidak sama sekali.

- **Time Complexity:** O(n × W)
- **Space Complexity:** O(n × W)

### Algoritma 2: Greedy — Fractional Knapsack
**Studi Kasus:** Kurir memiliki tas kapasitas 10 kg dan boleh mengambil sebagian barang untuk memaksimalkan keuntungan.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

## Cara Menjalankan

### Prasyarat
- Python 3.6 atau lebih baru

### Menjalankan Program
```bash
python main.py
```

Program akan menampilkan:
1. Data input (daftar barang dan kapasitas)
2. Tabel DP dan proses backtracking (0/1 Knapsack)
3. Step-by-step keputusan greedy (Fractional Knapsack)
4. Perbandingan hasil kedua algoritma
5. Analisis kompleksitas (Big O Notation)

## Struktur File
```
├── main.py              # Entry point program
├── knapsack_dp.py       # Implementasi 0/1 Knapsack (DP)
├── knapsack_greedy.py   # Implementasi Fractional Knapsack (Greedy)
├── visualizer.py        # Utilitas visualisasi terminal
└── README.md            # Dokumentasi (file ini)
```

## Bahasa Pemrograman
Python
