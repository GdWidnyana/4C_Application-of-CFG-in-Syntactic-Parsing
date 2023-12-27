def raw_to_cfg(raw):
    # Siapkan daftar kosong untuk menyimpan aturan yang telah diproses
    cfg = []

    # Iterasi melalui setiap baris dalam raw
    for line in raw:
        # Bagi baris dengan ' -> ' untuk memisahkan head dan body
        parts = line.split(' -> ')

        # Periksa apakah baris tersebut memiliki format yang diharapkan
        if len(parts) == 2:
            head = parts[0]
            body = parts[1]

            # Bagi body dengan ' | ' dan ubah menjadi set berisi tupel
            set_body = set(tuple(elemen.split(' ')) for elemen in body.split(' | '))

            # Tambahkan aturan yang telah diproses ke daftar cfg
            cfg.append([head, set_body])
        else:
            # Tangani baris dengan format yang salah, Anda dapat mencatat kesalahan atau melewatkannya sesuai kebutuhan
            print(f"Mengabaikan baris yang tidak valid: {line}")

    # Kembalikan aturan yang telah diproses
    return cfg
