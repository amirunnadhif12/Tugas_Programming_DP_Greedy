"""
==========================================================
  TUGAS PEMROGRAMAN: DYNAMIC PROGRAMMING & GREEDY
  Mata Kuliah: Perancangan dan Analisa Algoritma
==========================================================
  ALGORITMA DYNAMIC PROGRAMMING: 0/1 KNAPSACK
==========================================================
  Studi Kasus:
  Mahasiswa memiliki tas dengan kapasitas 10 kg dan ingin
  memilih barang yang dimasukkan agar nilai total maksimum.
  Setiap barang hanya bisa diambil seluruhnya atau tidak
  sama sekali (tidak boleh dipecah).

  Time Complexity : O(n x W)  -- pseudo-polynomial
  Space Complexity: O(n x W)  -- menyimpan seluruh tabel DP
==========================================================
"""


def knapsack_01(items, capacity):
    """
    Menyelesaikan 0/1 Knapsack menggunakan Dynamic Programming (bottom-up).

    Parameters:
        items    : list of dict, setiap dict memiliki key 'name', 'weight', 'value'
        capacity : int, kapasitas maksimum tas (dalam kg)

    Returns:
        max_value      : int, nilai total maksimum yang dapat dicapai
        selected_items : list of dict, item-item yang terpilih
        dp_table       : list of list, tabel DP berukuran (n+1) x (W+1)
        steps          : list of dict, log langkah pengisian tabel DP
    """
    n = len(items)
    W = capacity

    # -------------------------------------------------------
    # 1. Inisialisasi tabel DP berukuran (n+1) x (W+1)
    #    dp[i][w] = nilai maksimum menggunakan i item pertama
    #               dengan kapasitas w
    # -------------------------------------------------------
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Log langkah-langkah pengisian tabel
    steps = []

    # -------------------------------------------------------
    # 2. Mengisi tabel DP (bottom-up)
    #    Recurrence Relation:
    #    dp[i][w] = max(dp[i-1][w], dp[i-1][w - wi] + vi)
    #               jika w >= wi (item bisa dipertimbangkan)
    #    dp[i][w] = dp[i-1][w]
    #               jika w < wi  (item terlalu berat)
    # -------------------------------------------------------
    for i in range(1, n + 1):
        item = items[i - 1]
        wi = item["weight"]
        vi = item["value"]

        for w in range(W + 1):
            if wi <= w:
                # Pilih yang lebih besar: tidak ambil item, atau ambil item
                tidak_ambil = dp[i - 1][w]
                ambil = dp[i - 1][w - wi] + vi

                if ambil > tidak_ambil:
                    dp[i][w] = ambil
                    steps.append({
                        "item_index": i,
                        "item_name": item["name"],
                        "capacity": w,
                        "action": "AMBIL",
                        "value": ambil,
                        "explanation": (
                            f"dp[{i}][{w}] = max(dp[{i-1}][{w}], "
                            f"dp[{i-1}][{w-wi}] + {vi}) = "
                            f"max({tidak_ambil}, {dp[i-1][w-wi]} + {vi}) = {ambil}"
                        ),
                    })
                else:
                    dp[i][w] = tidak_ambil
                    steps.append({
                        "item_index": i,
                        "item_name": item["name"],
                        "capacity": w,
                        "action": "SKIP",
                        "value": tidak_ambil,
                        "explanation": (
                            f"dp[{i}][{w}] = max(dp[{i-1}][{w}], "
                            f"dp[{i-1}][{w-wi}] + {vi}) = "
                            f"max({tidak_ambil}, {dp[i-1][w-wi]} + {vi}) = {tidak_ambil}"
                        ),
                    })
            else:
                # Item terlalu berat untuk kapasitas w
                dp[i][w] = dp[i - 1][w]
                steps.append({
                    "item_index": i,
                    "item_name": item["name"],
                    "capacity": w,
                    "action": "TERLALU BERAT",
                    "value": dp[i - 1][w],
                    "explanation": (
                        f"dp[{i}][{w}] = dp[{i-1}][{w}] = {dp[i-1][w]} "
                        f"(berat item {wi} > kapasitas {w})"
                    ),
                })

    max_value = dp[n][W]

    # -------------------------------------------------------
    # 3. Backtracking: menentukan item yang dipilih
    #    Mulai dari dp[n][W], telusuri ke atas untuk menentukan
    #    item mana saja yang berkontribusi pada solusi optimal
    # -------------------------------------------------------
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # Item i-1 dipilih (karena nilainya berubah)
            selected_items.append(items[i - 1])
            w -= items[i - 1]["weight"]

    selected_items.reverse()  # Urutkan sesuai urutan input

    return max_value, selected_items, dp, steps


# -------------------------------------------------------
# Data default untuk pengujian mandiri
# -------------------------------------------------------
DEFAULT_ITEMS = [
    {"name": "Laptop",     "weight": 4, "value": 10},
    {"name": "Buku Tebal", "weight": 4, "value": 12},
    {"name": "Headphone",  "weight": 2, "value": 5},
    {"name": "Charger",    "weight": 3, "value": 6},
    {"name": "Mouse",      "weight": 1, "value": 3},
    {"name": "Tablet",     "weight": 5, "value": 8},
]
DEFAULT_CAPACITY = 10


if __name__ == "__main__":
    # Pengujian mandiri
    max_val, selected, dp_table, steps = knapsack_01(DEFAULT_ITEMS, DEFAULT_CAPACITY)

    print(f"Nilai Maksimum: {max_val}")
    print(f"Item Terpilih:")
    total_weight = 0
    for item in selected:
        print(f"  - {item['name']} (berat={item['weight']} kg, nilai={item['value']})")
        total_weight += item["weight"]
    print(f"Total Berat: {total_weight}/{DEFAULT_CAPACITY} kg")
