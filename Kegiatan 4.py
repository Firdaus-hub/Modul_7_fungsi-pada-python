def luas_persegi(sisi):
    luas = int(sisi * sisi)
    return luas

def volume_persegi (sisi):
    volume = luas_persegi(sisi) * sisi 
    return volume 

#Memanggil fungsi
a = volume_persegi (6)
print ('Volume Persegi:',a)