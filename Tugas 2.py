def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi dengan 0!"
    return a / b

def kalkulator(a, operator, b):
    if operator == '+':
        return tambah(a, b)
    elif operator == '-':
        return kurang(a, b)
    elif operator == '*':
        return kali(a, b)
    elif operator == '/':
        return bagi(a, b)
    else:
        return "Error: Operator tidak dikenal!"


# --- Program Utama ---

print("=" * 40)
print("      PROGRAM KALKULATOR SEDERHANA")
print("=" * 40)

while True:
    print("\nOperator yang tersedia: +  -  *  /")
    print("Ketik 'keluar' untuk mengakhiri program")
    print("-" * 40)

    input_a = input("Masukkan angka pertama : ")
    if input_a.lower() == 'keluar':
        break

    operator = input("Masukkan operator      : ")
    if operator.lower() == 'keluar':
        break

    input_b = input("Masukkan angka kedua   : ")
    if input_b.lower() == 'keluar':
        break

    try:
        a = float(input_a)
        b = float(input_b)

        hasil = kalkulator(a, operator, b)

        print("-" * 40)
        if isinstance(hasil, str):
            print(f"Hasil : {hasil}")
        else:
            print(f"Hasil : {a} {operator} {b} = {hasil:.4f}")
        print("=" * 40)

    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")
