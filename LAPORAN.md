# LAPORAN TUGAS PEMROGRAMAN
# Dynamic Programming & Greedy Algorithm

---

**Mata Kuliah:** Perancangan dan Analisa Algoritma
**Semester:** 6
**Bahasa Pemrograman:** Python

---

## Anggota Kelompok

| No | Nama Lengkap | NIM |
|----|-------------|-----|
| 1  |             |     |
| 2  |             |     |
| 3  |             |     |

---

## DAFTAR ISI

1. Analisis Deskripsi Masalah
   - 1.1 Algoritma 1: 0/1 Knapsack (Dynamic Programming)
   - 1.2 Algoritma 2: Fractional Knapsack (Greedy)
2. Data Input
3. Visualisasi Proses Jalannya Algoritma
   - 3.1 Visualisasi 0/1 Knapsack (Dynamic Programming)
   - 3.2 Visualisasi Fractional Knapsack (Greedy)
4. Hasil dan Perbandingan
5. Analisis Kompleksitas (Time & Space Complexity)
   - 5.1 0/1 Knapsack — Dynamic Programming
   - 5.2 Fractional Knapsack — Greedy
   - 5.3 Tabel Perbandingan Kompleksitas
6. Kesimpulan

---

## 1. Analisis Deskripsi Masalah

Knapsack Problem (Masalah Ransel) adalah salah satu permasalahan optimasi klasik dalam ilmu komputer. Permasalahan ini melibatkan pemilihan sejumlah item dengan berat dan nilai tertentu untuk dimasukkan ke dalam sebuah tas (knapsack) yang memiliki kapasitas terbatas, dengan tujuan memaksimalkan total nilai yang didapat.

Dalam tugas ini, kami mengimplementasikan dua variasi Knapsack Problem menggunakan dua paradigma pemrograman yang berbeda:

### 1.1 Algoritma 1: 0/1 Knapsack (Dynamic Programming)

**Studi Kasus:**
Seorang mahasiswa memiliki tas dengan kapasitas **10 kg** dan ingin memilih barang-barang yang akan dimasukkan ke dalam tas agar **nilai total barang yang dibawa menjadi maksimum**. Setiap barang hanya bisa **diambil seluruhnya atau tidak sama sekali** (tidak boleh dipecah).

**Definisi Formal:**
- Diberikan `n` item, masing-masing memiliki berat `w_i` dan nilai `v_i`
- Kapasitas tas = `W`
- Variabel keputusan: `x_i ∈ {0, 1}` (ambil atau tidak)
- Tujuan: Maksimalkan `Σ(v_i × x_i)` dengan batasan `Σ(w_i × x_i) ≤ W`

**Mengapa menggunakan Dynamic Programming?**
- Masalah 0/1 Knapsack memiliki **overlapping subproblems** (submasalah yang sama dihitung berulang kali)
- Memiliki **optimal substructure** (solusi optimal mengandung solusi optimal dari submasalahnya)
- Pendekatan Greedy TIDAK menjamin solusi optimal untuk varian 0/1 karena item tidak bisa dipecah

**Recurrence Relation (Rumus Rekurens):**
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w - w_i] + v_i)   jika w >= w_i
dp[i][w] = dp[i-1][w]                                   jika w < w_i
```

Keterangan:
- `dp[i][w]` = nilai maksimum yang bisa dicapai menggunakan `i` item pertama dengan kapasitas `w`
- `dp[i-1][w]` = nilai jika item ke-i TIDAK diambil
- `dp[i-1][w - w_i] + v_i` = nilai jika item ke-i DIAMBIL

---

### 1.2 Algoritma 2: Fractional Knapsack (Greedy)

**Studi Kasus:**
Seorang kurir memiliki tas dengan kapasitas **10 kg** dan boleh **mengambil sebagian barang** untuk memaksimalkan keuntungan pengiriman. Setiap barang memiliki berat dan nilai, dan kurir boleh mengambil **fraksi/sebagian** dari suatu barang.

**Definisi Formal:**
- Diberikan `n` item, masing-masing memiliki berat `w_i` dan nilai `v_i`
- Kapasitas tas = `W`
- Variabel keputusan: `x_i ∈ [0, 1]` (boleh sebagian/fraksi)
- Tujuan: Maksimalkan `Σ(v_i × x_i)` dengan batasan `Σ(w_i × x_i) ≤ W`

**Mengapa menggunakan Greedy?**
- Fractional Knapsack memiliki **Greedy Choice Property**: pilihan lokal terbaik (item dengan rasio value/weight tertinggi) selalu mengarah ke solusi global optimal
- Memiliki **Optimal Substructure**: setelah mengambil item terbaik, submasalah sisa juga optimal
- Karena item boleh dipecah, tidak perlu mempertimbangkan semua kemungkinan kombinasi

**Greedy Strategy:**
1. Hitung rasio `value/weight` untuk setiap item
2. Urutkan item berdasarkan rasio secara **descending** (tertinggi ke terendah)
3. Ambil item satu per satu mulai dari rasio tertinggi:
   - Jika item muat seluruhnya → ambil 100%
   - Jika item tidak muat seluruhnya → ambil sebagian (fraksi) sesuai sisa kapasitas
   - Jika tas sudah penuh → lewati item sisa

---

## 2. Data Input

Berikut adalah data barang yang digunakan dalam implementasi kedua algoritma:

| No | Nama Barang | Berat (kg) | Nilai | Rasio (Value/Weight) |
|----|-------------|-----------|-------|---------------------|
| 1  | Laptop      | 4         | 10    | 2.50                |
| 2  | Buku Tebal  | 4         | 12    | 3.00                |
| 3  | Headphone   | 2         | 5     | 2.50                |
| 4  | Charger     | 3         | 6     | 2.00                |
| 5  | Mouse       | 1         | 3     | 3.00                |
| 6  | Tablet      | 5         | 8     | 1.60                |

- **Jumlah Item (n):** 6
- **Total Berat Semua Item:** 19 kg
- **Kapasitas Tas (W):** 10 kg

Karena total berat (19 kg) melebihi kapasitas tas (10 kg), tidak semua barang bisa dibawa — diperlukan pemilihan optimal.

---

## 3. Visualisasi Proses Jalannya Algoritma

### 3.1 Visualisasi 0/1 Knapsack (Dynamic Programming)

#### 3.1.1 Tabel DP (DP Table)

Tabel DP berukuran **(n+1) × (W+1) = 7 × 11**, di mana:
- Baris = item yang dipertimbangkan (0 = tanpa item, 1 = Laptop, 2 = Buku Tebal, dst.)
- Kolom = kapasitas tas dari 0 sampai 10 kg
- Setiap sel `dp[i][w]` = nilai maksimum menggunakan `i` item pertama dengan kapasitas `w`

| Item \ Kapasitas | 0 | 1 | 2 | 3 | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
|------------------|---|---|---|---|----|----|----|----|----|----|----|
| (kosong)         | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| Laptop (4kg,10)  | 0 | 0 | 0 | 0 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Buku Tebal (4kg,12) | 0 | 0 | 0 | 0 | 12 | 12 | 12 | 12 | **22** | **22** | **22** |
| Headphone (2kg,5)| 0 | 0 | 5 | 5 | 12 | 12 | 17 | 17 | 22 | 22 | **27** |
| Charger (3kg,6)  | 0 | 0 | 5 | 6 | 12 | 12 | 17 | 18 | 22 | 23 | 27 |
| Mouse (1kg,3)    | 0 | 3 | 5 | 8 | 12 | 15 | 17 | 20 | 22 | 25 | 27 |
| Tablet (5kg,8)   | 0 | 3 | 5 | 8 | 12 | 15 | 17 | 20 | 22 | 25 | 27 |

**Nilai optimal: dp[6][10] = 27**

#### 3.1.2 Contoh Pengisian Sel Tabel DP

Berikut contoh bagaimana beberapa sel kunci diisi:

**Sel dp[1][4] (Laptop, kapasitas 4):**
```
dp[1][4] = max(dp[0][4], dp[0][4-4] + 10)
         = max(0, dp[0][0] + 10)
         = max(0, 0 + 10)
         = max(0, 10)
         = 10  → AMBIL Laptop
```

**Sel dp[2][8] (Buku Tebal, kapasitas 8):**
```
dp[2][8] = max(dp[1][8], dp[1][8-4] + 12)
         = max(10, dp[1][4] + 12)
         = max(10, 10 + 12)
         = max(10, 22)
         = 22  → AMBIL Buku Tebal
```

**Sel dp[3][10] (Headphone, kapasitas 10):**
```
dp[3][10] = max(dp[2][10], dp[2][10-2] + 5)
          = max(22, dp[2][8] + 5)
          = max(22, 22 + 5)
          = max(22, 27)
          = 27  → AMBIL Headphone
```

#### 3.1.3 Proses Backtracking (Menentukan Item Terpilih)

Setelah tabel DP selesai diisi, dilakukan **backtracking** dari sel `dp[6][10]` ke `dp[0][0]` untuk menentukan item mana saja yang dipilih:

```
Mulai dari dp[6][10] = 27

Langkah 1: dp[6][10] = 27 == dp[5][10] = 27
           → Tablet TIDAK DIPILIH (nilai tidak berubah)

Langkah 2: dp[5][10] = 27 == dp[4][10] = 27
           → Mouse TIDAK DIPILIH (nilai tidak berubah)

Langkah 3: dp[4][10] = 27 == dp[3][10] = 27
           → Charger TIDAK DIPILIH (nilai tidak berubah)

Langkah 4: dp[3][10] = 27 ≠ dp[2][10] = 22
           → Headphone DIPILIH ✓ (berat=2 kg, nilai=5)
           → Sisa kapasitas: 10 - 2 = 8 kg

Langkah 5: dp[2][8] = 22 ≠ dp[1][8] = 10
           → Buku Tebal DIPILIH ✓ (berat=4 kg, nilai=12)
           → Sisa kapasitas: 8 - 4 = 4 kg

Langkah 6: dp[1][4] = 10 ≠ dp[0][4] = 0
           → Laptop DIPILIH ✓ (berat=4 kg, nilai=10)
           → Sisa kapasitas: 4 - 4 = 0 kg
```

**Hasil 0/1 Knapsack:**

| Item Terpilih | Berat (kg) | Nilai |
|---------------|-----------|-------|
| Laptop        | 4         | 10    |
| Buku Tebal    | 4         | 12    |
| Headphone     | 2         | 5     |
| **Total**     | **10/10** | **27**|

---

### 3.2 Visualisasi Fractional Knapsack (Greedy)

#### 3.2.1 Pengurutan Item Berdasarkan Rasio (Greedy Choice)

Langkah pertama algoritma Greedy adalah menghitung rasio **value/weight** dan mengurutkan secara **descending**:

| Urutan | Nama Barang | Berat (kg) | Nilai | Rasio (v/w) |
|--------|-------------|-----------|-------|-------------|
| 1      | Buku Tebal  | 4         | 12    | **3.00**    |
| 2      | Mouse       | 1         | 3     | **3.00**    |
| 3      | Laptop      | 4         | 10    | **2.50**    |
| 4      | Headphone   | 2         | 5     | **2.50**    |
| 5      | Charger     | 3         | 6     | 2.00        |
| 6      | Tablet      | 5         | 8     | 1.60        |

#### 3.2.2 Proses Greedy Step-by-Step

| Step | Item | Rasio | Keputusan | Fraksi | Berat Diambil | Nilai Didapat | Sisa Kapasitas |
|------|------|-------|-----------|--------|---------------|---------------|----------------|
| 1 | Buku Tebal | 3.00 | **AMBIL** | 100% | 4 kg | +12.00 | 10 - 4 = **6 kg** |
| 2 | Mouse | 3.00 | **AMBIL** | 100% | 1 kg | +3.00 | 6 - 1 = **5 kg** |
| 3 | Laptop | 2.50 | **AMBIL** | 100% | 4 kg | +10.00 | 5 - 4 = **1 kg** |
| 4 | Headphone | 2.50 | **AMBIL SEBAGIAN** | **50%** | 1 kg (dari 2 kg) | +2.50 | 1 - 1 = **0 kg** |
| 5 | Charger | 2.00 | LEWATI | 0% | - | +0.00 | 0 kg (PENUH) |
| 6 | Tablet | 1.60 | LEWATI | 0% | - | +0.00 | 0 kg (PENUH) |

**Penjelasan detail setiap langkah:**

**Step 1 — Buku Tebal (rasio 3.00):**
Item dengan rasio tertinggi. Berat 4 kg ≤ sisa kapasitas 10 kg → ambil seluruhnya (100%). Sisa kapasitas = 10 - 4 = 6 kg.

**Step 2 — Mouse (rasio 3.00):**
Rasio sama dengan Buku Tebal. Berat 1 kg ≤ sisa kapasitas 6 kg → ambil seluruhnya (100%). Sisa kapasitas = 6 - 1 = 5 kg.

**Step 3 — Laptop (rasio 2.50):**
Rasio tertinggi berikutnya. Berat 4 kg ≤ sisa kapasitas 5 kg → ambil seluruhnya (100%). Sisa kapasitas = 5 - 4 = 1 kg.

**Step 4 — Headphone (rasio 2.50):**
Berat 2 kg > sisa kapasitas 1 kg → **TIDAK MUAT seluruhnya**. Ambil **fraksi**: 1/2 = 50% dari item. Berat diambil = 1 kg. Nilai didapat = 5 × 0.50 = 2.50. Sisa kapasitas = 0 kg.

**Step 5 & 6 — Charger & Tablet:**
Tas sudah penuh (sisa kapasitas = 0 kg) → item dilewati.

**Hasil Fractional Knapsack:**

| Item Diambil | Fraksi | Berat Diambil (kg) | Nilai Didapat |
|-------------|--------|---------------------|---------------|
| Buku Tebal  | 100%   | 4.0                 | 12.00         |
| Mouse       | 100%   | 1.0                 | 3.00          |
| Laptop      | 100%   | 4.0                 | 10.00         |
| Headphone   | **50%**| 1.0                 | 2.50          |
| **Total**   |        | **10.0/10**         | **27.50**     |

---

## 4. Hasil dan Perbandingan

| Aspek | 0/1 Knapsack (DP) | Fractional Knapsack (Greedy) |
|-------|-------------------|------------------------------|
| Paradigma | Dynamic Programming | Greedy |
| **Nilai Maksimum** | **27** | **27.50** |
| Total Berat | 10/10 kg | 10.0/10 kg |
| Boleh Pecah Item? | Tidak | Ya |
| Jumlah Item Diambil | 3 item (utuh) | 4 item (3 utuh + 1 fraksi) |
| Time Complexity | O(n × W) | O(n log n) |
| Space Complexity | O(n × W) | O(n) |

**Insight:**
- Fractional Knapsack menghasilkan nilai **+0.50 lebih tinggi** daripada 0/1 Knapsack (27.50 vs 27)
- Hal ini karena Fractional Knapsack boleh mengambil **sebagian** item (Headphone 50%), sehingga ruang sisa 1 kg masih bisa dimanfaatkan
- Pada 0/1 Knapsack, sisa 1 kg tidak bisa diisi karena tidak ada item yang beratnya pas 1 kg dan belum dipilih (Mouse sudah tidak optimal jika menggantikan item lain)
- Secara matematis, nilai Fractional Knapsack **selalu ≥** nilai 0/1 Knapsack untuk data yang sama

---

## 5. Analisis Kompleksitas (Time & Space Complexity)

### 5.1 0/1 Knapsack — Dynamic Programming

#### Time Complexity: O(n × W)

| Tahap | Operasi | Kompleksitas |
|-------|---------|-------------|
| Inisialisasi tabel DP | Membuat array (n+1) × (W+1) | O(n × W) |
| Pengisian tabel DP | Iterasi setiap sel, setiap sel O(1) | **O(n × W)** |
| Backtracking | Telusuri dari dp[n][W] ke dp[0][0] | O(n) |
| **Total** | | **O(n × W)** |

**Penjelasan:**
- Tabel DP berukuran (n+1) × (W+1) = (6+1) × (10+1) = **77 sel**
- Setiap sel membutuhkan **O(1)** operasi (satu operasi perbandingan `max`)
- Total operasi pengisian: n × W = 6 × 10 = **60 operasi**
- Backtracking: O(n) = O(6) untuk menelusuri item terpilih
- Total: O(n × W) + O(n) = **O(n × W)**
- Catatan: kompleksitas ini adalah **pseudo-polynomial** karena W adalah *nilai* input (bukan *ukuran* input dalam bit)

#### Space Complexity: O(n × W)

| Komponen | Ukuran | Keterangan |
|----------|--------|------------|
| Tabel DP | (n+1) × (W+1) = 7 × 11 = 77 sel | Menyimpan seluruh tabel |
| List item terpilih | O(n) | Menyimpan hasil backtracking |
| Log langkah | O(n × W) | Opsional, untuk visualisasi |
| **Total** | | **O(n × W)** |

---

### 5.2 Fractional Knapsack — Greedy

#### Time Complexity: O(n log n)

| Tahap | Operasi | Kompleksitas |
|-------|---------|-------------|
| Hitung rasio v/w | Iterasi semua item | O(n) |
| **Sorting** berdasarkan rasio | Merge sort / Timsort | **O(n log n)** |
| Greedy selection | Iterasi item terurut | O(n) |
| **Total** | | **O(n log n)** |

**Penjelasan:**
- Menghitung rasio value/weight untuk setiap item: O(n) = O(6)
- Sorting berdasarkan rasio secara descending: **O(n log n)** = O(6 × log₂ 6) ≈ O(6 × 2.58) ≈ 16 operasi
- Iterasi greedy selection (ambil item satu per satu): O(n) = O(6)
- Total: O(n) + O(n log n) + O(n) = **O(n log n)**
- Didominasi oleh operasi **sorting**

#### Space Complexity: O(n)

| Komponen | Ukuran | Keterangan |
|----------|--------|------------|
| List item dengan rasio | O(n) | Menyimpan rasio setiap item |
| List terurut | O(n) | Hasil sorting |
| List item terpilih | O(n) | Item + fraksi yang diambil |
| Log langkah | O(n) | Opsional, untuk visualisasi |
| **Total** | | **O(n)** |

---

### 5.3 Tabel Perbandingan Kompleksitas

| Aspek | 0/1 Knapsack (DP) | Fractional Knapsack (Greedy) |
|-------|-------------------|------------------------------|
| **Time Complexity** | **O(n × W)** | **O(n log n)** |
| **Space Complexity** | **O(n × W)** | **O(n)** |
| Jenis | Pseudo-polynomial | Polynomial |
| Bergantung pada W? | Ya (semakin besar W, semakin lambat) | Tidak |
| Cocok untuk data besar? | Terbatas oleh W | Sangat efisien |

**Dengan data n = 6 item dan W = 10 kg:**
- DP melakukan ≈ **60 operasi** dan menggunakan ≈ **77 sel memori**
- Greedy melakukan ≈ **16 operasi** dan menggunakan ≈ **18 slot memori**

**Perbandingan skalabilitas:**
- Jika n = 1000 dan W = 10.000:
  - DP: 1000 × 10.000 = **10.000.000 operasi**, memori = **10.001.000 sel**
  - Greedy: 1000 × log₂(1000) ≈ **10.000 operasi**, memori = **3.000 slot**
  - Greedy **1000× lebih cepat** dan **3333× lebih hemat memori**

---

## 6. Kesimpulan

1. **Dynamic Programming (0/1 Knapsack)** cocok untuk masalah di mana item tidak bisa dipecah. DP menjamin solusi **optimal** dengan mempertimbangkan semua kemungkinan kombinasi melalui tabel transisi status. Namun, kompleksitasnya **O(n × W)** yang bersifat pseudo-polynomial membuatnya kurang efisien untuk kapasitas (W) yang sangat besar.

2. **Greedy (Fractional Knapsack)** cocok untuk masalah di mana item boleh dipecah. Dengan strategi mengambil item berdasarkan rasio value/weight tertinggi, Greedy menjamin solusi **optimal** dengan kompleksitas yang jauh lebih efisien yaitu **O(n log n)**. Namun, pendekatan Greedy **tidak menjamin solusi optimal** untuk varian 0/1 Knapsack.

3. Nilai Fractional Knapsack **selalu ≥** nilai 0/1 Knapsack karena ruang solusi 0/1 merupakan subset dari ruang solusi Fractional. Dalam studi kasus ini: **27.50 ≥ 27**.

4. Pemilihan paradigma algoritma harus disesuaikan dengan **karakteristik masalah**:
   - Jika item bersifat *discrete* (tidak bisa dipecah) → gunakan **Dynamic Programming**
   - Jika item bersifat *continuous* (boleh dipecah) → gunakan **Greedy**

---

**Bahasa Pemrograman:** Python
**Cara Menjalankan Program:** `python main.py`
