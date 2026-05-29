from datetime import datetime
from dateutil.relativedelta import relativedelta

def hitung_umur(tanggal_lahir):
    # Mengubah string menjadi objek datetime
    lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    sekarang = datetime.now()
    
    # Menghitung selisih waktu
    selisih = relativedelta(sekarang, lahir)
    
    return selisih.years, selisih.months, selisih.days
print(hitung_umur("1945-08-17"))