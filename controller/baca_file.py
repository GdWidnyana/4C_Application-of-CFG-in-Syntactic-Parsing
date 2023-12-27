# membuka file aturan cnf
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

