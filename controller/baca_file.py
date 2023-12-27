import os

def baca_file(filepath):
    # persiapkan list kosong
    data = []
    
    # ubah path ke format yang sesuai dengan sistem operasi
    filepath = os.path.abspath(filepath)
    
    # periksa apakah file ada
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    
    # buka file txt dengan mode baca
    with open(filepath, 'r') as file: 
        # baca setiap aturan baris per baris
        raw = file.readlines()

        # tambahkan setiap aturan ke dalam list data dan hapus karakter newline
        for aturan in raw:
            data.append(aturan.strip('\n'))

    # kembalikan aturan cnf mentah
    return data

# Ubah filepath sesuai dengan path yang diinginkan
filepath = 'data/4C_CNF.txt'

try:
    # Panggil fungsi baca_file dengan filepath yang baru
    data_cnf = baca_file(filepath)
    
    # Lakukan operasi lain dengan data_cnf jika diperlukan
    print(data_cnf)
except FileNotFoundError as e:
    print(e)
