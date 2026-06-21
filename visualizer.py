"""
==========================================================
  TUGAS PEMROGRAMAN: DYNAMIC PROGRAMMING & GREEDY
  Mata Kuliah: Perancangan dan Analisa Algoritma
==========================================================
  VISUALIZER -- Utilitas Visualisasi Algoritma
==========================================================
  Modul ini menyediakan fungsi-fungsi untuk menampilkan:
  1. Tabel DP (0/1 Knapsack) secara rapi di terminal
  2. Step-by-step keputusan Greedy (Fractional Knapsack)
  3. Tabel perbandingan hasil kedua algoritma
  4. Analisis kompleksitas
==========================================================
"""


# ============================================================
# KONSTANTA WARNA (ANSI Escape Codes)
# ============================================================
class Colors:
    """ANSI color codes untuk mempercantik output terminal."""
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    UNDERLINE = "\033[4m"

    # Foreground
    RED       = "\033[91m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    BLUE      = "\033[94m"
    MAGENTA   = "\033[95m"
    CYAN      = "\033[96m"
    WHITE     = "\033[97m"

    # Background
    BG_BLUE   = "\033[44m"
    BG_GREEN  = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_CYAN   = "\033[46m"


def _color(text, color_code):
    """Menambahkan warna pada teks."""
    return f"{color_code}{text}{Colors.RESET}"


def _bold(text):
    """Menebalkan teks."""
    return f"{Colors.BOLD}{text}{Colors.RESET}"


# ============================================================
# HEADER & SEPARATOR
# ============================================================
def print_header(title, width=70):
    """Menampilkan header dengan border."""
    print()
    print(_color("=" * width, Colors.CYAN))
    padding = (width - len(title)) // 2
    print(_color(" " * padding + title, Colors.BOLD + Colors.CYAN))
    print(_color("=" * width, Colors.CYAN))
    print()


def print_subheader(title, width=70):
    """Menampilkan sub-header."""
    print()
    print(_color("-" * width, Colors.BLUE))
    print(_color(f"  {title}", Colors.BOLD + Colors.BLUE))
    print(_color("-" * width, Colors.BLUE))
    print()


def print_separator(char="-", width=70):
    """Menampilkan garis pemisah."""
    print(_color(char * width, Colors.DIM))


# ============================================================
# VISUALISASI DATA INPUT
# ============================================================
def display_items_table(items, capacity, context_title=""):
    """
    Menampilkan tabel data input (daftar item dan kapasitas).

    Parameters:
        items         : list of dict
        capacity      : int
        context_title : str, judul konteks (opsional)
    """
    if context_title:
        print_subheader(context_title)

    # Header tabel
    print(f"  {'No':<4} {'Nama Item':<14} {'Berat (kg)':<12} {'Nilai':<8}")
    print(f"  {'─'*4} {'─'*14} {'─'*12} {'─'*8}")

    for i, item in enumerate(items, 1):
        print(f"  {i:<4} {item['name']:<14} {item['weight']:<12} {item['value']:<8}")

    print()
    print(f"  Kapasitas Tas: {_bold(str(capacity) + ' kg')}")
    print()


# ============================================================
# VISUALISASI TABEL DP (0/1 KNAPSACK)
# ============================================================
def display_dp_table(items, dp_table, selected_items, capacity):
    """
    Menampilkan tabel DP secara rapi dengan highlight pada sel
    yang berkontribusi pada solusi optimal.

    Parameters:
        items          : list of dict, daftar item
        dp_table       : list of list, tabel DP (n+1) x (W+1)
        selected_items : list of dict, item yang terpilih
        capacity       : int, kapasitas tas
    """
    print_subheader("TABEL DP — 0/1 KNAPSACK")

    n = len(items)
    W = capacity

    # Tentukan sel-sel yang merupakan bagian dari backtracking path
    backtrack_cells = set()
    w = W
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            backtrack_cells.add((i, w))
            w -= items[i - 1]["weight"]
        else:
            backtrack_cells.add((i, w))

    # Tentukan lebar kolom berdasarkan nilai terbesar
    max_val = max(max(row) for row in dp_table)
    col_width = max(4, len(str(max_val)) + 2)

    # Header kolom (kapasitas 0..W)
    name_width = 14
    header = f"  {'Item':<{name_width}}"
    for w in range(W + 1):
        header += f"{w:>{col_width}}"
    print(_color(header, Colors.BOLD))
    print(f"  {'─' * name_width}" + "─" * (col_width * (W + 1)))

    # Baris data
    row_names = ["(kosong)"] + [item["name"] for item in items]
    selected_names = {item["name"] for item in selected_items}

    for i in range(n + 1):
        # Nama item di kolom pertama
        name = row_names[i]
        if name in selected_names:
            row_str = f"  {_color(name + ' ✓', Colors.GREEN):<{name_width + 11}}"
        else:
            row_str = f"  {name:<{name_width}}"

        # Nilai setiap sel
        for w in range(W + 1):
            val = dp_table[i][w]
            val_str = f"{val:>{col_width}}"

            if (i, w) in backtrack_cells and i > 0:
                # Sel yang merupakan bagian dari solusi optimal
                if dp_table[i][w] != dp_table[i - 1][w]:
                    # Item ini dipilih di sini
                    row_str += _color(val_str, Colors.GREEN + Colors.BOLD)
                else:
                    row_str += _color(val_str, Colors.YELLOW)
            elif val > 0:
                row_str += _color(val_str, Colors.WHITE)
            else:
                row_str += _color(val_str, Colors.DIM)

        print(row_str)

    print()

    # Keterangan warna
    print(f"  Keterangan:")
    print(f"    {_color('■', Colors.GREEN + Colors.BOLD)} = Item dipilih (backtrack path)")
    print(f"    {_color('■', Colors.YELLOW)} = Jalur backtracking")
    print(f"    {_color('■', Colors.DIM)} = Sel bernilai 0")
    print()


def display_dp_backtrack(items, dp_table, selected_items, capacity):
    """
    Menampilkan proses backtracking langkah demi langkah.
    """
    print_subheader("BACKTRACKING — Menentukan Item Terpilih")

    n = len(items)
    w = capacity

    print(f"  Mulai dari dp[{n}][{w}] = {dp_table[n][w]}")
    print()

    step = 0
    for i in range(n, 0, -1):
        item = items[i - 1]
        if dp_table[i][w] != dp_table[i - 1][w]:
            step += 1
            print(
                f"  Langkah {step}: dp[{i}][{w}] = {dp_table[i][w]} ≠ "
                f"dp[{i-1}][{w}] = {dp_table[i-1][w]}"
            )
            print(
                f"             → {_color(item['name'] + ' DIPILIH', Colors.GREEN + Colors.BOLD)} "
                f"(berat={item['weight']} kg, nilai={item['value']})"
            )
            print(f"             → Sisa kapasitas: {w} - {item['weight']} = {w - item['weight']} kg")
            w -= item["weight"]
            print()
        else:
            print(
                f"  Cek:      dp[{i}][{w}] = {dp_table[i][w]} == "
                f"dp[{i-1}][{w}] = {dp_table[i-1][w]}"
            )
            print(
                f"             → {_color(item['name'] + ' TIDAK DIPILIH', Colors.RED)}"
            )
            print()

    print()


def display_dp_result(max_value, selected_items, capacity):
    """Menampilkan ringkasan hasil 0/1 Knapsack."""
    print_subheader("HASIL — 0/1 Knapsack (Dynamic Programming)")

    total_weight = sum(item["weight"] for item in selected_items)

    print(f"  {_bold('Nilai Maksimum')}: {_color(str(max_value), Colors.GREEN + Colors.BOLD)}")
    print(f"  {_bold('Total Berat')}   : {total_weight}/{capacity} kg")
    print()
    print(f"  Item yang dipilih:")
    for i, item in enumerate(selected_items, 1):
        print(
            f"    {i}. {_color(item['name'], Colors.CYAN)} "
            f"(berat={item['weight']} kg, nilai={item['value']})"
        )
    print()


# ============================================================
# VISUALISASI STEP-BY-STEP GREEDY (FRACTIONAL KNAPSACK)
# ============================================================
def display_sorted_items(sorted_items):
    """
    Menampilkan item setelah diurutkan berdasarkan rasio value/weight.
    """
    print_subheader("ITEM DIURUTKAN BERDASARKAN RASIO (Value/Weight)")

    print(f"  {'No':<4} {'Nama Item':<14} {'Berat (kg)':<12} {'Nilai':<8} {'Rasio (v/w)':<12}")
    print(f"  {'─'*4} {'─'*14} {'─'*12} {'─'*8} {'─'*12}")

    for i, item in enumerate(sorted_items, 1):
        ratio_str = f"{item['ratio']:.2f}"
        print(
            f"  {i:<4} {item['name']:<14} {item['weight']:<12} "
            f"{item['value']:<8} {_color(ratio_str, Colors.YELLOW + Colors.BOLD):<12}"
        )

    print()
    print(
        f"  {_color('↑ Greedy Strategy:', Colors.BOLD)} "
        f"Ambil item dari rasio tertinggi ke terendah"
    )
    print()


def display_greedy_steps(step_log, capacity):
    """
    Menampilkan proses keputusan greedy langkah demi langkah.
    """
    print_subheader("STEP-BY-STEP GREEDY — Fractional Knapsack")

    # Header tabel
    print(
        f"  {'Step':<6} {'Item':<14} {'Rasio':<8} {'Keputusan':<12} "
        f"{'Fraksi':<10} {'Nilai +':<10} {'Sisa Kap.':<10}"
    )
    print(
        f"  {'─'*6} {'─'*14} {'─'*8} {'─'*12} "
        f"{'─'*10} {'─'*10} {'─'*10}"
    )

    for log in step_log:
        step = log["step"]
        name = log["item_name"]
        ratio = f"{log['ratio']:.2f}"
        frac_pct = f"{log['fraction'] * 100:.0f}%"
        value_gained = f"+{log['value_gained']:.2f}"
        remaining = f"{log['remaining_capacity']:.1f} kg"

        if log["taken"]:
            if log["fraction"] == 1.0:
                decision = _color("AMBIL 100%", Colors.GREEN + Colors.BOLD)
            else:
                decision = _color(f"AMBIL {frac_pct}", Colors.YELLOW + Colors.BOLD)
            value_str = _color(value_gained, Colors.GREEN)
        else:
            decision = _color("LEWATI", Colors.RED)
            value_str = _color("+0.00", Colors.DIM)
            frac_pct = "0%"

        print(
            f"  {step:<6} {name:<14} {ratio:<8} {decision:<23} "
            f"{frac_pct:<10} {value_str:<21} {remaining:<10}"
        )

        # Penjelasan di bawah setiap langkah
        print(f"         {_color('→ ' + log['explanation'], Colors.DIM)}")
        print()

    print()


def display_greedy_result(max_value, selected_items, capacity):
    """Menampilkan ringkasan hasil Fractional Knapsack."""
    print_subheader("HASIL — Fractional Knapsack (Greedy)")

    total_weight = sum(item["weight"] * item["fraction"] for item in selected_items)

    print(f"  {_bold('Nilai Maksimum')}: {_color(f'{max_value:.2f}', Colors.GREEN + Colors.BOLD)}")
    print(f"  {_bold('Total Berat')}   : {total_weight:.1f}/{capacity} kg")
    print()
    print(f"  Item yang diambil:")
    for i, item in enumerate(selected_items, 1):
        frac_pct = item["fraction"] * 100
        weight_taken = item["weight"] * item["fraction"]
        if item["fraction"] == 1.0:
            frac_display = _color("100%", Colors.GREEN)
        else:
            frac_display = _color(f"{frac_pct:.1f}%", Colors.YELLOW)

        print(
            f"    {i}. {_color(item['name'], Colors.CYAN)} "
            f"[{frac_display}] "
            f"berat={weight_taken:.1f} kg, nilai={item['value_gained']:.2f}"
        )
    print()


# ============================================================
# PERBANDINGAN KEDUA ALGORITMA
# ============================================================
def display_comparison(dp_result, greedy_result, capacity):
    """
    Menampilkan tabel perbandingan hasil kedua algoritma.

    Parameters:
        dp_result     : tuple (max_value, selected_items)
        greedy_result : tuple (max_value, selected_items)
        capacity      : int
    """
    print_header("PERBANDINGAN HASIL: DP vs GREEDY")

    dp_val, dp_items = dp_result
    greedy_val, greedy_items = greedy_result

    dp_weight = sum(item["weight"] for item in dp_items)
    greedy_weight = sum(item["weight"] * item.get("fraction", 1.0) for item in greedy_items)

    # Tabel perbandingan
    col1_w = 25
    col2_w = 25
    col3_w = 25

    print(f"  {'Aspek':<{col1_w}} {'0/1 Knapsack (DP)':<{col2_w}} {'Fractional (Greedy)':<{col3_w}}")
    print(f"  {'─'*col1_w} {'─'*col2_w} {'─'*col3_w}")

    print(
        f"  {'Paradigma':<{col1_w}} "
        f"{_color('Dynamic Programming', Colors.CYAN):<{col2_w+11}} "
        f"{_color('Greedy', Colors.YELLOW):<{col3_w+11}}"
    )
    print(
        f"  {'Nilai Maksimum':<{col1_w}} "
        f"{_color(str(dp_val), Colors.GREEN + Colors.BOLD):<{col2_w+11}} "
        f"{_color(f'{greedy_val:.2f}', Colors.GREEN + Colors.BOLD):<{col3_w+11}}"
    )
    print(
        f"  {'Total Berat':<{col1_w}} "
        f"{dp_weight}/{capacity} kg{' '*(col2_w - len(f'{dp_weight}/{capacity} kg'))} "
        f"{greedy_weight:.1f}/{capacity} kg"
    )
    print(
        f"  {'Boleh Pecah Item?':<{col1_w}} "
        f"{_color('Tidak', Colors.RED):<{col2_w+11}} "
        f"{_color('Ya', Colors.GREEN):<{col3_w+11}}"
    )
    print(
        f"  {'Jumlah Item Diambil':<{col1_w}} "
        f"{len(dp_items)} item{' '*(col2_w - len(f'{len(dp_items)} item'))} "
        f"{len(greedy_items)} item"
    )
    print(
        f"  {'Time Complexity':<{col1_w}} "
        f"{'O(n × W)':<{col2_w}} "
        f"{'O(n log n)':<{col3_w}}"
    )
    print(
        f"  {'Space Complexity':<{col1_w}} "
        f"{'O(n × W)':<{col2_w}} "
        f"{'O(n)':<{col3_w}}"
    )

    print()

    # Insight
    if greedy_val >= dp_val:
        diff = greedy_val - dp_val
        print(
            f"  {_color('📊 Insight:', Colors.BOLD)} Fractional Knapsack menghasilkan nilai "
            f"{_color(f'+{diff:.2f}', Colors.GREEN)} lebih tinggi"
        )
        print(
            f"  karena item boleh dipecah, sehingga tas bisa diisi lebih optimal."
        )
    else:
        print(
            f"  {_color('📊 Insight:', Colors.BOLD)} Kedua algoritma menghasilkan nilai yang sama."
        )

    print()
    print(
        f"  {_color('💡 Catatan:', Colors.BOLD)} Greedy O(n log n) jauh lebih cepat dari DP O(n×W),"
    )
    print(
        f"  tetapi Greedy hanya optimal untuk Fractional Knapsack, bukan 0/1 Knapsack."
    )
    print()


# ============================================================
# ANALISIS KOMPLEKSITAS
# ============================================================
def display_complexity_analysis(n, W):
    """
    Menampilkan analisis formal kompleksitas kedua algoritma.

    Parameters:
        n : int, jumlah item
        W : int, kapasitas tas
    """
    print_header("ANALISIS KOMPLEKSITAS (Big O Notation)")

    # --- 0/1 Knapsack (DP) ---
    print_subheader("0/1 Knapsack — Dynamic Programming")

    print(f"  {_bold('Time Complexity: O(n × W)')}")
    print()
    print(f"  Penjelasan:")
    print(f"    • Tabel DP berukuran (n+1) × (W+1) = ({n+1}) × ({W+1}) = {(n+1)*(W+1)} sel")
    print(f"    • Setiap sel membutuhkan O(1) operasi (perbandingan max)")
    print(f"    • Total operasi: n × W = {n} × {W} = {n*W} operasi")
    print(f"    • Backtracking: O(n) = O({n}) untuk menentukan item terpilih")
    print(f"    • Total: O(n × W) + O(n) = {_color('O(n × W)', Colors.YELLOW + Colors.BOLD)}")
    print(f"    • Catatan: ini adalah {_bold('pseudo-polynomial')} karena W adalah")
    print(f"      nilai input, bukan ukuran input")
    print()

    print(f"  {_bold('Space Complexity: O(n × W)')}")
    print()
    print(f"  Penjelasan:")
    print(f"    • Tabel DP: (n+1) × (W+1) = ({n+1}) × ({W+1}) = {(n+1)*(W+1)} sel integer")
    print(f"    • Memori tambahan: O(n) untuk menyimpan item terpilih")
    print(f"    • Total: O(n × W) + O(n) = {_color('O(n × W)', Colors.YELLOW + Colors.BOLD)}")
    print()

    # --- Fractional Knapsack (Greedy) ---
    print_subheader("Fractional Knapsack — Greedy")

    print(f"  {_bold('Time Complexity: O(n log n)')}")
    print()
    print(f"  Penjelasan:")
    print(f"    • Menghitung rasio value/weight: O(n) = O({n})")
    print(f"    • Sorting berdasarkan rasio: O(n log n) = O({n} × log {n})")
    print(f"    • Iterasi greedy selection: O(n) = O({n})")
    print(f"    • Total: O(n) + O(n log n) + O(n) = {_color('O(n log n)', Colors.YELLOW + Colors.BOLD)}")
    print(f"    • Didominasi oleh operasi {_bold('sorting')}")
    print()

    print(f"  {_bold('Space Complexity: O(n)')}")
    print()
    print(f"  Penjelasan:")
    print(f"    • List item dengan rasio: O(n) = O({n})")
    print(f"    • List sorted: O(n) = O({n})")
    print(f"    • Log langkah & item terpilih: O(n) = O({n})")
    print(f"    • Total: {_color('O(n)', Colors.YELLOW + Colors.BOLD)}")
    print()

    # --- Perbandingan ---
    print_subheader("Tabel Perbandingan Kompleksitas")

    print(f"  {'Algoritma':<30} {'Time':<15} {'Space':<15}")
    print(f"  {'─'*30} {'─'*15} {'─'*15}")
    print(
        f"  {'0/1 Knapsack (DP)':<30} "
        f"{_color('O(n × W)', Colors.RED):<26} "
        f"{_color('O(n × W)', Colors.RED):<26}"
    )
    print(
        f"  {'Fractional Knapsack (Greedy)':<30} "
        f"{_color('O(n log n)', Colors.GREEN):<26} "
        f"{_color('O(n)', Colors.GREEN):<26}"
    )
    print()
    print(
        f"  Dengan n = {n} item dan W = {W} kg:"
    )
    print(
        f"    • DP melakukan ≈ {n * W} operasi, menggunakan ≈ {(n+1)*(W+1)} sel memori"
    )
    import math
    print(
        f"    • Greedy melakukan ≈ {n * int(math.log2(n)) if n > 1 else n} operasi, "
        f"menggunakan ≈ {3 * n} slot memori"
    )
    print()
