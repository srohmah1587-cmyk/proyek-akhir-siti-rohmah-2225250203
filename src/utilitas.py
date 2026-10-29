
# Nama: Siti Rohmah
# NIM: 2225250203
# Kelas: 3A
# File: utilitas.py
# Program Rekap dan Analisis Nilai Matematika Kelas


BATAS_KETUNTASAN = 60


def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berada dalam rentang 0 sampai 100.

    Return:
        True jika nilai valid, False jika tidak valid.
    """
    try:
        nilai = float(nilai)
        return 0 <= nilai <= 100
    except (ValueError, TypeError):
        return False


def status_ketuntasan(nilai, batas=BATAS_KETUNTASAN):
    """
    Menentukan status ketuntasan berdasarkan batas nilai.

    Nilai >= batas dinyatakan Tuntas.
    Nilai < batas dinyatakan Belum Tuntas.
    """
    if not validasi_nilai(nilai):
        return "Nilai tidak valid"

    if float(nilai) >= batas:
        return "Tuntas"

    return "Belum Tuntas"


def format_nilai(nilai):
    """Mengubah nilai menjadi teks dengan dua angka desimal."""
    try:
        return f"{float(nilai):.2f}"
    except (ValueError, TypeError):
        return "Tidak valid"


def tampilkan_garis(panjang=45):
    """Menampilkan garis pemisah pada terminal."""
    print("-" * panjang)


def tampilkan_judul(judul):
    """Menampilkan judul dengan garis pemisah."""
    tampilkan_garis()
    print(judul.center(45))
    tampilkan_garis()


def tampilkan_status_siswa(data_nilai, batas=BATAS_KETUNTASAN):
    """Menampilkan NIM, nilai, dan status ketuntasan setiap siswa."""

    if not data_nilai:
        print("Tidak ada data siswa untuk ditampilkan.")
        return

    tampilkan_judul("STATUS KETUNTASAN SISWA")
    print(f"{'NIM':<15}{'NILAI':<12}{'STATUS'}")
    tampilkan_garis()

    for nim, nilai in data_nilai:
        status = status_ketuntasan(nilai, batas)
        print(f"{nim:<15}{format_nilai(nilai):<12}{status}")

    tampilkan_garis()


if __name__ == "__main__":
    # Data untuk menguji fungsi utilitas
    data_uji = [
        ("A001", 85),
        ("A002", 60),
        ("A003", 45),
    ]

    tampilkan_judul("UJI COBA UTILITAS")
    tampilkan_status_siswa(data_uji)

    print("\nUji validasi nilai:")
    print("Nilai 80 :", validasi_nilai(80))
    print("Nilai 120:", validasi_nilai(120))
    print("Teks abc :", validasi_nilai("abc"))

    print("\nUji status ketuntasan:")
    print("Nilai 85:", status_ketuntasan(85))
    print("Nilai 60:", status_ketuntasan(60))
    print("Nilai 45:", status_ketuntasan(45))