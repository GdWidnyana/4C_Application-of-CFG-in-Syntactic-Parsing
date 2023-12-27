def print_table(table_data, column_name):
    # Menyiapkan tag style untuk mempercantik tampilan tabel
    table = """
    <style>
    table {
    border-collapse: collapse;
    width: 100%;
    }

    th {
    background-color: #1e90ff; /* Ubah menjadi warna hijau (kode heksadesimal) */
    color: white;
    }
    </style>
    """

    # Membuat tag pembuka untuk tabel
    table += "<table>"

    # Menambahkan baris judul tabel
    table += "<tr>"
    for name in column_name:
        table += f"<th>{name}</th>"
    table += "</tr>"

    # Menambahkan data ke dalam tabel
    for row in table_data:
        table += "<tr>"
        for column in row:
            table += f"<td>{column}</td>"
        table += "</tr>"

    # Menambahkan tag penutup untuk tabel dan tambahan break line
    table += "</table><br>"

    # Mengembalikan string HTML yang merepresentasikan tabel
    return table
