"""
==========================================================
  TUGAS PEMROGRAMAN: DYNAMIC PROGRAMMING & GREEDY
  Mata Kuliah: Perancangan dan Analisa Algoritma
==========================================================
  ALGORITMA GREEDY: FRACTIONAL KNAPSACK
==========================================================
  Studi Kasus:
  Kurir memiliki tas kapasitas 10 kg dan boleh mengambil
  sebagian barang untuk memaksimalkan keuntungan. Setiap
  barang memiliki berat dan nilai, dan kurir boleh mengambil
  fraksi/sebagian dari suatu barang.

  Time Complexity : O(n log n)  -- didominasi sorting
  Space Complexity: O(n)        -- menyimpan list item & log
==========================================================
"""


def fractional_knapsack(items, capacity):
    """
    Menyelesaikan Fractional Knapsack menggunakan algoritma Greedy.

    Greedy Strategy:
    Urutkan item berdasarkan rasio value/weight secara descending,
    lalu ambil item mulai dari rasio tertinggi. Jika item tidak
    muat seluruhnya, ambil fraksi yang tersisa.

    Parameters:
        items    : list of dict, setiap dict memiliki key 'name', 'weight', 'value'
        capacity : int/float, kapasitas maksimum tas (dalam kg)

    Returns:
        max_value      : float, nilai total maksimum yang dicapai
        selected_items : list of dict, item yang diambil beserta fraksinya
        step_log       : list of dict, log langkah-langkah keputusan greedy
        sorted_items   : list of dict, item yang sudah diurutkan berdasarkan rasio
    """

    # -------------------------------------------------------
    # 1. Hitung rasio value/weight untuk setiap item
    # -------------------------------------------------------
    items_with_ratio = []
    for item in items:
        ratio = item["value"] / item["weight"]
        items_with_ratio.append({
            "name": item["name"],
            "weight": item["weight"],
            "value": item["value"],
            "ratio": ratio,
        })

    # -------------------------------------------------------
    # 2. Greedy Choice Property:
    #    Urutkan item berdasarkan rasio value/weight
    #    secara DESCENDING (rasio tertinggi lebih dulu)
    #    Time: O(n log n)
    # -------------------------------------------------------
    sorted_items = sorted(items_with_ratio, key=lambda x: x["ratio"], reverse=True)

    # -------------------------------------------------------
    # 3. Greedy Selection:
    #    Ambil item satu per satu mulai dari rasio tertinggi
    # -------------------------------------------------------
    remaining_capacity = capacity
    max_value = 0.0
    selected_items = []
    step_log = []
    step_number = 0

    for item in sorted_items:
        step_number += 1

        if remaining_capacity <= 0:
            # Tas sudah penuh, item tidak bisa diambil lagi
            step_log.append({
                "step": step_number,
                "item_name": item["name"],
                "weight": item["weight"],
                "value": item["value"],
                "ratio": item["ratio"],
                "taken": False,
                "fraction": 0.0,
                "value_gained": 0.0,
                "remaining_capacity": remaining_capacity,
                "explanation": f"Tas sudah penuh, {item['name']} tidak diambil.",
            })
            continue

        if item["weight"] <= remaining_capacity:
            # -----------------------------------------------
            # Item muat seluruhnya → ambil 100%
            # -----------------------------------------------
            fraction = 1.0
            value_gained = item["value"]
            remaining_capacity -= item["weight"]

            selected_items.append({
                "name": item["name"],
                "weight": item["weight"],
                "value": item["value"],
                "ratio": item["ratio"],
                "fraction": fraction,
                "value_gained": value_gained,
            })

            step_log.append({
                "step": step_number,
                "item_name": item["name"],
                "weight": item["weight"],
                "value": item["value"],
                "ratio": item["ratio"],
                "taken": True,
                "fraction": fraction,
                "value_gained": value_gained,
                "remaining_capacity": remaining_capacity,
                "explanation": (
                    f"{item['name']} (berat={item['weight']} kg) muat seluruhnya. "
                    f"Ambil 100%. Sisa kapasitas: {remaining_capacity} kg."
                ),
            })

        else:
            # -----------------------------------------------
            # Item TIDAK muat seluruhnya → ambil fraksi
            # -----------------------------------------------
            fraction = remaining_capacity / item["weight"]
            value_gained = item["value"] * fraction

            selected_items.append({
                "name": item["name"],
                "weight": item["weight"],
                "value": item["value"],
                "ratio": item["ratio"],
                "fraction": fraction,
                "value_gained": value_gained,
            })

            step_log.append({
                "step": step_number,
                "item_name": item["name"],
                "weight": item["weight"],
                "value": item["value"],
                "ratio": item["ratio"],
                "taken": True,
                "fraction": fraction,
                "value_gained": value_gained,
                "remaining_capacity": 0,
                "explanation": (
                    f"{item['name']} (berat={item['weight']} kg) tidak muat seluruhnya. "
                    f"Sisa kapasitas: {remaining_capacity} kg. "
                    f"Ambil {fraction*100:.1f}% ({remaining_capacity} kg dari {item['weight']} kg). "
                    f"Nilai yang didapat: {value_gained:.2f}."
                ),
            })

            remaining_capacity = 0

        max_value += value_gained

    return max_value, selected_items, step_log, sorted_items


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
    max_val, selected, step_log, sorted_items = fractional_knapsack(
        DEFAULT_ITEMS, DEFAULT_CAPACITY
    )

    print(f"Nilai Maksimum: {max_val:.2f}")
    print(f"Item Terpilih:")
    total_weight = 0
    for item in selected:
        frac_pct = item["fraction"] * 100
        weight_taken = item["weight"] * item["fraction"]
        print(
            f"  - {item['name']} ({frac_pct:.0f}%) "
            f"berat={weight_taken:.1f} kg, nilai={item['value_gained']:.2f}"
        )
        total_weight += weight_taken
    print(f"Total Berat: {total_weight:.1f}/{DEFAULT_CAPACITY} kg")
