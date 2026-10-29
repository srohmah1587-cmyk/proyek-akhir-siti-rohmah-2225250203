
# Nama: Siti Rohmah
# NIM: 2225250203
# Kelas: 3A
# File: analisis.py
# Program Rekap dan Analisis Nilai Matematika Kelas


def analisis_nilai(data_nilai, batas_kelulusan=60):
    """
    Mengolah data nilai siswa dan menghasilkan statistik nilai.

    Parameter:
        data_nilai: daftar data berbentuk (NIM, nilai)
        batas_kelulusan: nilai minimum untuk dinyatakan tuntas

    Return:
        Dictionary berisi hasil analisis nilai.
        None jika tidak ada data yang valid.
    """

    if not data_nilai:
        print("Tidak ada data nilai yang dapat dianalisis.")
        return None

    daftar_nilai = [nilai for nim, nilai in data_nilai]

    jumlah_siswa = len(data_nilai)
    total_nilai = sum(daftar_nilai)
    rata_rata = total_nilai / jumlah_siswa
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    siswa_tuntas = [
        (nim, nilai)
        for nim, nilai in data_nilai
        if nilai >= batas_kelulusan
    ]

    siswa_belum_tuntas = [
        (nim, nilai)
        for nim, nilai in data_nilai
        if nilai < batas_kelulusan
    ]

    hasil = {
        "jumlah_siswa": jumlah_siswa,
        "total_nilai": total_nilai,
        "rata_rata": rata_rata,
        "nilai_tertinggi": nilai_tertinggi,
        "nilai_terendah": nilai_terendah,
        "jumlah_tuntas": len(siswa_tuntas),
        "jumlah_belum_tuntas": len(siswa_belum_tuntas),
        "siswa_tuntas": siswa_tuntas,
        "siswa_belum_tuntas": siswa_belum_tuntas,
    }

    return hasil


def tampilkan_analisis(hasil):
    """Menampilkan ringkasan hasil analisis nilai."""

    if hasil is None:
        return

    print("\n=== HASIL ANALISIS NILAI ===")
    print(f"Jumlah siswa       : {hasil['jumlah_siswa']}")
    print(f"Total nilai        : {hasil['total_nilai']:.2f}")
    print(f"Rata-rata nilai    : {hasil['rata_rata']:.2f}")
    print(f"Nilai tertinggi    : {hasil['nilai_tertinggi']:.2f}")
    print(f"Nilai terendah     : {hasil['nilai_terendah']:.2f}")
    print(f"Siswa tuntas       : {hasil['jumlah_tuntas']}")
    print(f"Siswa belum tuntas : {hasil['jumlah_belum_tuntas']}")

    print("\nDaftar siswa tuntas:")
    for nim, nilai in hasil["siswa_tuntas"]:
        print(f"- {nim}: {nilai:g}")

    print("\nDaftar siswa belum tuntas:")
    for nim, nilai in hasil["siswa_belum_tuntas"]:
        print(f"- {nim}: {nilai:g}")


if __name__ == "__main__":
    # Data untuk menguji fungsi secara mandiri
    data_uji = [
        ("A001", 85),
        ("A002", 78),
        ("A003", 92),
        ("A005", 60),
        ("A006", 50),
        ("A007", 75),
        ("A008", 88),
        ("A009", 45),
        ("A010", 100),
    ]

    hasil_uji = analisis_nilai(data_uji)
    tampilkan_analisis(hasil_uji)