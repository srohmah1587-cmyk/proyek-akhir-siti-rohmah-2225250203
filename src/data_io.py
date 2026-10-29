
# data_io.py
# Fungsi untuk membaca dan menyimpan data nilai matematika

import csv
from pathlib import Path


def baca_nilai(nama_file):
    """
    Membaca data nilai dari file CSV sederhana.
    Format setiap baris: NIM,nilai

    Mengembalikan daftar tuple (NIM, nilai).
    Baris yang tidak valid akan dilewati.
    Mengembalikan None jika file tidak ditemukan.
    """
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8", newline="") as file:
            pembaca = csv.reader(file)

            for nomor_baris, baris in enumerate(pembaca, start=1):
                if not baris or all(not kolom.strip() for kolom in baris):
                    continue

                if len(baris) != 2:
                    print(
                        f"Peringatan: Format salah pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                nim = baris[0].strip()

                try:
                    nilai = float(baris[1].strip())
                except ValueError:
                    print(
                        f"Peringatan: Nilai bukan angka pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                if not nim or not 0 <= nilai <= 100:
                    print(
                        f"Peringatan: Data tidak valid pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                data_nilai.append((nim, nilai))

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None
    except OSError as error:
        print(f"Error saat membaca file: {error}")
        return None

    return data_nilai


def simpan_rekap(nama_file, data_nilai, hasil):
    """
    Menyimpan detail nilai dan hasil analisis ke file teks.
    """
    try:
        lokasi = Path(nama_file)
        lokasi.parent.mkdir(parents=True, exist_ok=True)

        with open(lokasi, "w", encoding="utf-8") as file:
            file.write("REKAP NILAI MATEMATIKA KELAS\n")
            file.write("=" * 35 + "\n\n")

            file.write("DETAIL NILAI SISWA\n")
            file.write("-" * 35 + "\n")

            for nim, nilai in data_nilai:
                status = (
                    "Tuntas" if nilai >= 60 else "Belum tuntas"
                )
                file.write(f"{nim} | {nilai:g} | {status}\n")

            file.write("\nHASIL ANALISIS\n")
            file.write("-" * 35 + "\n")
            file.write(f"Jumlah siswa valid: {hasil['jumlah_siswa']}\n")
            file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")
            file.write(f"Nilai tertinggi: {hasil['nilai_tertinggi']:g}\n")
            file.write(f"Nilai terendah: {hasil['nilai_terendah']:g}\n")
            file.write(f"Jumlah tuntas: {hasil['jumlah_tuntas']}\n")
            file.write(
                f"Jumlah belum tuntas: "
                f"{hasil['jumlah_belum_tuntas']}\n"
            )

        print(f"Rekap berhasil disimpan ke '{lokasi}'.")

    except OSError as error:
        print(f"Error saat menyimpan rekap: {error}")