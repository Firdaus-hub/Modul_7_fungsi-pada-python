def celsius_ke_reamur(c):
    return c * (4 / 5)

def celsius_ke_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15


# --- Program Utama ---

print("=" * 40)
print("     PROGRAM KONVERSI SUHU")
print("=" * 40)

celsius = float(input("Masukkan suhu dalam Celsius: "))

reamur     = celsius_ke_reamur(celsius)
fahrenheit = celsius_ke_fahrenheit(celsius)
kelvin     = celsius_ke_kelvin(celsius)

print()
print(f"Suhu        : {celsius} °C")
print("-" * 40)
print(f"Reamur      : {reamur:.2f} °R")
print(f"Fahrenheit  : {fahrenheit:.2f} °F")
print(f"Kelvin      : {kelvin:.2f} K")
print("=" * 40)