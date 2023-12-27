# Import streamlit sebagai framework frontend
import streamlit as st

# Import fungsi-fungsi yang diperlukan
from controller.baca_file import baca_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# Siapkan tampilan web
def run_streamlit():
    # Judul untuk halaman web
    title = "Aplikasi Parsing Bahasa Indonesia dengan pola Frasa Verba Menggunakan Algoritma Cocke–Younger–Kasami"

    # Konfigurasi tampilan web
    st.set_page_config(layout='wide', page_title=title)
    
    # Persiapkan aturan CNF
    raw_cfg = baca_file('data/4C_CNF.txt')
    # Konversi aturan CNF mentah ke format yang dapat dibaca oleh Python
    cnf = raw_to_cfg(raw_cfg)

    # Judul web
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)
    
    # Tambahkan garis pembatas
    st.markdown("<hr>", unsafe_allow_html=True)
    # Deskripsi singkat tentang tugas
    deskripsi_tugas = """
        <p>Aplikasi ini dirancang untuk melakukan parsing pada kalimat Bahasa Indonesia dengan pola frasa verba menggunakan Algoritma Cocke–Younger–Kasami (CYK). Anda dapat melihat aturan Chomsky Normal Form (CNF) yang digunakan dalam pemrosesan, dan memasukkan kalimat untuk dianalisis.</p>
        <p>Gunakan tombol 'View CNF Rules' untuk melihat aturan CFG yang telah dikonversi menjadi CNF Rules, dan masukkan kalimat Anda di kolom sebelah kanan untuk memulai proses parsing kalimat. Kalimat yang diterima adalah kalimat sederhana yang mengandung frasa verba sebagai predikat, pelengkap, dan keterangan.</p>
    """

    st.markdown(deskripsi_tugas, unsafe_allow_html=True)
    
    # Tambahkan tabel anggota kelompok
    st.write("<h2>Anggota Kelompok 4C Teori Bahasa Otomata</h2>", unsafe_allow_html=True)
    anggota_kelompok = [
        {"Nama": "I Gede Widnyana", "NIM": "2208561016"},
        {"Nama": "I Gede Widiantara Mega Saputra", "NIM": "2208561022"},
        {"Nama": "Ni Putu Meita Kartika Dewi", "NIM": "2208561072"},
        {"Nama": "Ni Luh Gede Cahaya Putri Mahadewi", "NIM": "2208561110"},
    ]
    # Konversi data anggota kelompok ke dalam format yang dapat digunakan oleh Streamlit
    data_anggota_kelompok = {"Nama": [], "NIM": []}
    for anggota in anggota_kelompok:
        data_anggota_kelompok["Nama"].append(anggota["Nama"])
        data_anggota_kelompok["NIM"].append(anggota["NIM"])

    # Tampilkan tabel
    st.table(data_anggota_kelompok)
    
    # Bagi tampilan web menjadi dua kolom, kolom kiri menampilkan aturan CNF, kolom kanan menampilkan tabel pengisian
    col1, col2 = st.columns(2, gap='small')

    with col1:
    # Menambahkan tombol KBBI Online
        st.markdown("""
            <a href="https://kbbi.kemdikbud.go.id/" target="_blank">
                <button type="button">
                    KKBI Online
                </button>
            </a>
            """, unsafe_allow_html=True)

    # Menambahkan jarak antara button
        st.write("") 

    # Menampilkan button untuk melihat aturan CNF
        view_rule_button = st.button("View CNF Rules", type='primary')
        if view_rule_button:
            st.write(raw_cfg)

    # Persiapkan kolom kanan
    with col2:
        # Kotak teks input kalimat
        string_input = st.text_input('Masukan Kalimat Anda di kolom bawah ini ⬇️')
        # Konversi kalimat menjadi list
        list_string = string_input.split(' ')
        # Tombol cek
        button_click = st.button('Periksa Kalimat Anda', type='primary')

        # Aksi jika tombol diklik
        if button_click:
            # Tampilkan pesan kesalahan jika tidak ada string atau hanya satu string yang dimasukkan
            if len(list_string) <= 1:
                st.warning("Kalimat tidak boleh kosong ataupun hanya terdiri satu kata!")

            # Jika tidak, proses tabel pengisian
            elif string_input != '':
                st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))
