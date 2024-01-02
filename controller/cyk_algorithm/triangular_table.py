# Impor pustaka dan kerangka kerja yang diperlukan
import streamlit as st
from view.table import print_table

# Simbol himpunan kosong
empty = '\u2205'

# Persiapkan tabel untuk algoritma CYK
def create_table(daftar_kata):
    # Persiapkan daftar kosong
    tabel = []
    # Untuk setiap kata dalam kalimat
    for i in range(len(daftar_kata)):
        # Tambahkan daftar kosong sebagai baris
        tabel.append([])
        # Untuk setiap kata dalam kalimat
        for j in range(len(daftar_kata)):
            # Jika i < j, tambahkan ' ' sebagai kolom dalam baris saat ini
            if i < j:
                tabel[i].append(' ')
            # Jika tidak, tambahkan himpunan kosong sebagai kolom dalam baris saat ini
            else:
                tabel[i].append(set())
    
    # Kembalikan tabel kosong
    return tabel

# Isi iterasi pertama
def filling_botton(tabel, cnf, daftar_kata):
    # Untuk setiap kata dalam daftar
    for i, kata in enumerate(daftar_kata):
        # Persiapkan himpunan kosong untuk sel tabel
        sel = set()
        # Untuk setiap aturan dalam CNF
        for baris in cnf:
            # Untuk setiap elemen dalam badan aturan
            for elemen in baris[1]:
                # Jika kata saat ini sama dengan elemen saat ini (dalam huruf kecil)
                if kata.lower() in (x.lower() for x in elemen):
                    # Tambahkan ke sel himpunan saat ini
                    sel.add(baris[0])
                    # Hentikan iterasi
                    break
        
        # Isi diagonal ([i][i]) tabel dengan sel himpunan
        tabel[i][i] = sel

# Isi semua tabel pengisian, dimulai dari baris 1
def filling_all(cnf, tabel, string, baris=1):
    is_accepted = False  # Inisialisasi variabel status penerimaan

    # Jika kolom pertama dalam baris terakhir bukan himpunan kosong [set()]
    if tabel[len(tabel) - 1][0] != set():
        # Jika simbol awal ada di dalamnya
        if 'X' in tabel[len(tabel) - 1][0]:
            # Tampilkan tanda bahwa kalimat diterima
            is_accepted = True
        else:
            # Jika tidak, tampilkan tanda bahwa kalimat tidak diterima
            is_accepted = False
        
        # Hentikan rekursi dan kembalikan dua nilai
        return is_accepted, tabel

    # Temukan baris berikutnya yang akan diisi dengan fungsi iterasi
    baris_berikutnya = iterasi(cnf, tabel, string, baris)

    # Panggil kembali fungsi filling_all dengan baris_berikutnya yang telah diperbarui
    return filling_all(cnf, tabel, string, baris_berikutnya)

# Iterasi untuk mengisi sel tabel
def iterasi(cnf, tabel, input_string, baris):
    # Iterasi turun untuk kolom dalam baris saat ini
    for kolom in range(len(tabel) - 1, -1, -1):
        # Jika sel saat ini adalah himpunan kosong
        if tabel[baris][kolom] == set():
            
            # Persiapkan daftar kosong untuk menyimpan irisan
            list_of_intersect = []
            # Iterasi baris dalam sel saat ini dari baris 0
            for i in range(0, baris):
                # Jika sel dalam [i][kolom] adalah simbol himpunan kosong
                if tabel[i][kolom] == empty:
                    # Tambahkan himpunan kosong ke list_of_intersect
                    list_of_intersect.append(set())
                # Jika tidak, jika sel dalam [i][kolom] bukan ' ' dan bukan himpunan kosong
                elif tabel[i][kolom] != ' ' and tabel[i][kolom] != set():
                    # Tambahkan isi sel ke dalam list_of_intersect
                    list_of_intersect.append(tabel[i][kolom])

            # Iterasi kolom dalam sel saat ini dari kolom saat ini + 1
            for i in range(kolom + 1, len(tabel)):
                # Jika sel dalam [baris][i] adalah simbol himpunan kosong
                if tabel[baris][i] == empty:
                    # Tambahkan himpunan kosong ke list_of_intersect
                    list_of_intersect.append(set())
                # Jika tidak, jika sel dalam [baris][i] bukan ' ' dan bukan himpunan kosong
                elif tabel[baris][i] != ' ' and tabel[baris][i] != set():
                    # Tambahkan isi sel ke dalam list_of_intersect
                    list_of_intersect.append(tabel[baris][i])

            # Buat kombinasi dari list_of_intersect dan simpan kombinasinya
            hasil_list = membuat_kombinasi(list_of_intersect)

            # Gabungkan semua kombinasi dalam hasil_list menjadi himpunan
            gabung_hasil = menggabungkan(hasil_list)
            
            # Temukan aturan CNF yang tepat untuk sel tabel saat ini
            tabel[baris][kolom] = mencari_cnf(gabung_hasil, cnf)

            # Tampilkan tabel pengisian yang telah diperbarui
            st.write(print_table(tabel, input_string), unsafe_allow_html=True)

            # Tingkatkan nilai baris jika nomor baris berikutnya < total semua baris, jika tidak, kembali ke baris nomor 1
            baris = (baris + 1) if baris + 1 < len(tabel) else 1
            # Kembalikan nilai baris
            return baris

    # Tingkatkan nilai baris jika nomor baris berikutnya < total semua baris, jika tidak, kembali ke baris nomor 1
    baris = (baris + 1) if baris + 1 < len(tabel) else 1
    # Kembalikan nilai baris
    return baris

# Buat kombinasi dari badan dalam baris dan kolom saat ini
def membuat_kombinasi(list_input):
    # Hitung semua elemen dalam list_input, lalu bagi 2
    count = len(list_input) // 2

    # Daftar kosong untuk semua kombinasi
    kombinasi = []

    # Iterasi sebanyak count
    for i in range(count):
        # list1 adalah indeks i dari list_input
        list1 = list_input[i]
        # list2 adalah indeks i + count dari list_input
        list2 = list_input[i + count]

        # Tambahkan daftar kosong ke dalam kombinasi
        kombinasi.append([])

        # Iterasi semua elemen dalam list1
        for elemen1 in list1:
            # Iterasi semua elemen dalam list2
            for elemen2 in list2:
                # Kombinasi adalah tupel dari elemen1 saat ini dan elemen2 saat ini, lalu tambahkan
                kombinasi[i].append(tuple((elemen1, elemen2)))
    
    # Kembalikan kombinasi
    return kombinasi

# Gabungkan semua kombinasi menjadi himpunan
def menggabungkan(raw_kombinasi):
    # Persiapkan himpunan kosong
    hasil_set = set()

    # Untuk setiap kombinasi dalam raw_kombinasi
    for x in raw_kombinasi:
        # Untuk setiap tupel dalam kombinasi
        for y in x:
            # Tambahkan kombinasi ke dalam himpunan hasil_set
            hasil_set.add(y)

    # Kembalikan hasil_set
    return hasil_set

# Temukan aturan CNF yang tepat untuk mengisi sel saat ini
def mencari_cnf(gabung, cnf):
    # Persiapkan himpunan kosong
    cnf_return = set()

    # Iterasi semua kombinasi
    for com in gabung:
        # Iterasi setiap aturan dalam CNF
        for baris in cnf:
            # Jika kombinasi ada dalam badan aturan saat ini
            if com in baris[1]:
                # Tambahkan kepala aturan saat ini ke dalam himpunan cnf_return
                cnf_return.add(baris[0])
    
    # Jika cnf_return adalah himpunan kosong
    if cnf_return == set():
        # Kembalikan simbol himpunan kosong
        return empty
    else:
        # Jika tidak, kembalikan nilai cnf_return
        return cnf_return
