# Impor pustaka dan kerangka kerja yang diperlukan
import streamlit as st

# Impor proses tabel segitiga
from controller.cyk_algorithm.triangular_table import *
from view.table import print_table

# Fungsi untuk mengurai kalimat dengan algoritma CYK
def parse(cnf, daftar_kata):
    placeholder = st.empty()
    tabel = create_table(daftar_kata)
    # Tampilkan tabel ke web
    st.write(print_table(tabel, daftar_kata), unsafe_allow_html=True)

    # Isi iterasi pertama (baris paling bawah dalam tabel pengisian)
    filling_botton(tabel, cnf, daftar_kata)
    # Tampilkan tabel lagi ke web
    st.write(print_table(tabel, daftar_kata), unsafe_allow_html=True)

    # Isi semua tabel pengisian dan dapatkan status penerimaan
    is_accepted, tabel = filling_all(cnf, tabel, daftar_kata)
    
    # Logika untuk menampilkan pesan di atas tabel
    if is_accepted:
        placeholder.success('Kalimat diterima.')
        st.balloons()
    else:
        placeholder.error('Kalimat tidak diterima karena tidak sesuai pola atau persyaratan kalimat baku bahasa Indonesia atau ada kata yang belum terdaftar di database')
        st.snow()
