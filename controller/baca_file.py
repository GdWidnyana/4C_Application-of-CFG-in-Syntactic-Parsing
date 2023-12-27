def baca_file(filepath):
    # persiapkan list kosong
    data = []
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
filepath = r'C:\Users\Widnyana\Downloads\4c\Program\data\4c_CNF.txt'

# Panggil fungsi baca_file dengan filepath yang baru
data_cnf = baca_file(filepath)

# Lakukan operasi lain dengan data_cnf jika diperlukan
