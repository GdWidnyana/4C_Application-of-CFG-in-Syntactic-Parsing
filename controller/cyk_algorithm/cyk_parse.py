# Impor pustaka dan kerangka kerja yang diperlukan
import streamlit as st

# Impor proses tabel segitiga
from controller.cyk_algorithm.triangular_table import *
from view.table import print_table

# Fungsi untuk mengurai kalimat dengan algoritma CYK
def parse(cnf, daftar_kata):
    # Persiapkan tabel pengisian
    tabel = create_table(daftar_kata)
    # Tampilkan tabel ke web
    st.write(print_table(tabel, daftar_kata), unsafe_allow_html=True)

    # Isi iterasi pertama (baris paling bawah dalam tabel pengisian)
    filling_botton(tabel, cnf, daftar_kata)
    # Tampilkan tabel lagi ke web
    st.write(print_table(tabel, daftar_kata), unsafe_allow_html=True)

    # Isi semua tabel pengisian dan tampilkan status penerimaan
    filling_all(cnf, tabel, daftar_kata)