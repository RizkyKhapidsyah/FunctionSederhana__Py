#Fungsi Sederhana
def ProgramAyam():
    print('-' * 4, "Ayam", '-' * 4, '\n')

#Fungsi Dengan Input Argument
def HargaTotalAyam(kg):
    Harga = 20000
    HargaTotal = kg * Harga
    print('Harga', kg, 'kg Ayam =', HargaTotal)

#Fungsi Utama
def Main():
    ProgramAyam()
    HargaTotalAyam(1)
    HargaTotalAyam(2)
    HargaTotalAyam(3)
    HargaTotalAyam(4)
    HargaTotalAyam(5)
    HargaTotalAyam(6)
    HargaTotalAyam(7)
    HargaTotalAyam(8439579)

Main()



