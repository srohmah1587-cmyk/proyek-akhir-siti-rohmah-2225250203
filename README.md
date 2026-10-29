
# Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A  

## 1. Deskripsi Program

Program Rekap dan Analisis Nilai Matematika Kelas merupakan aplikasi berbasis Python yang digunakan untuk membaca, mengolah, dan menganalisis nilai siswa dari sebuah file teks. Program membantu proses rekapitulasi nilai agar lebih cepat, terstruktur, dan mengurangi kesalahan perhitungan manual.

Program dapat memeriksa validitas data, menghitung rata-rata nilai, menentukan nilai tertinggi dan terendah, serta mengelompokkan siswa berdasarkan status ketuntasan.

## 2. Tujuan Program

1. Membaca data NIM dan nilai siswa dari file teks.
2. Memvalidasi data agar hanya nilai yang sesuai ketentuan yang diproses.
3. Menghitung statistik nilai siswa.
4. Menentukan status ketuntasan berdasarkan batas nilai minimum.
5. Menampilkan dan menyimpan hasil rekap nilai.

## 3. Ketentuan Program

- Rentang nilai yang valid adalah 0 sampai 100.
- Batas ketuntasan adalah 60.
- Nilai lebih besar atau sama dengan 60 dinyatakan **Tuntas**.
- Nilai kurang dari 60 dinyatakan **Belum Tuntas**.
- Data yang tidak valid dilewati dan tidak dimasukkan ke perhitungan.
- Program memberikan pesan jika file tidak ditemukan atau tidak terdapat data valid.

## 4. Struktur Folder

```text
program-rekap-nilai/
├── data/
│   ├── nilai_contoh.txt
│   └── hasil_rekap.txt
├── hasil/
│   └── .gitkeep
├── main.py
├── analisis.py
├── data_io.py
├── utilitas.py
├── proposal.md
├── test_case.md
├── README.md
├── .gitignore
└── .gitkeep
```

Keterangan:

- `main.py`: program utama yang mengatur jalannya aplikasi.
- `analisis.py`: fungsi perhitungan statistik dan pengelompokan ketuntasan.
- `data_io.py`: fungsi membaca data dan menyimpan hasil rekap.
- `utilitas.py`: fungsi validasi nilai, format tampilan, dan status ketuntasan.
- `data/nilai_contoh.txt`: file masukan berisi NIM dan nilai siswa.
- `data/hasil_rekap.txt`: file keluaran hasil rekap jika penyimpanan diarahkan ke lokasi tersebut.
- `hasil/.gitkeep`: penanda agar folder hasil yang kosong tetap dapat disimpan Git.
- `proposal.md`: dokumen proposal proyek.
- `test_case.md`: skenario pengujian program.
- `.gitignore`: daftar file atau folder yang tidak perlu dilacak Git.

Catatan: File `hasil_rekap.txt` baru tersedia setelah program berhasil menyimpan hasil rekap. File `.gitkeep` dapat dihapus jika foldernya sudah berisi file lain.

## 5. Format Data Masukan

Data disimpan dalam file `data/nilai_contoh.txt` dengan format:

```text
A001,85
A002,78
A003,92
A004,abc
A005,60
A006,50
A007,75
A008,88
A009,45
A010,100
```

Setiap baris berisi NIM dan nilai yang dipisahkan dengan tanda koma. Baris `A004,abc` merupakan contoh data tidak valid karena nilai bukan angka.

## 6. Cara Menjalankan Program

### Persyaratan

- Python 3 telah terpasang.
- Semua file Python berada pada struktur folder yang sesuai.
- File masukan tersedia di lokasi yang digunakan oleh program.

### Langkah menjalankan

1. Buka folder proyek melalui VS Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah berikut:

```bash
python main.py
```

Pada beberapa sistem, gunakan:

```bash
python3 main.py
```

Pastikan modul `analisis.py`, `data_io.py`, dan `utilitas.py` diimpor sesuai dengan fungsi yang digunakan dalam `main.py`.

## 7. Contoh Hasil yang Diharapkan

Berdasarkan data contoh, terdapat sembilan data nilai valid dan satu data tidak valid.

| Komponen | Hasil |
|---|---:|
| Jumlah siswa valid | 9 |
| Total nilai | 673 |
| Rata-rata nilai | 74,78 |
| Nilai tertinggi | 100 |
| Nilai terendah | 45 |
| Siswa tuntas | 7 |
| Siswa belum tuntas | 2 |
| Data tidak valid | 1 |

Hasil tersebut merupakan hasil yang diharapkan berdasarkan data contoh. Tampilan terminal dapat berbeda bergantung pada implementasi `main.py`.

## 8. Pengujian Program

Pengujian dilakukan untuk memastikan setiap fungsi berjalan sesuai ketentuan. Skenario pengujian lengkap terdapat pada file `test_case.md`.

Aspek yang diuji meliputi:

1. Validasi nilai dalam rentang 0–100.
2. Penentuan status tuntas dan belum tuntas.
3. Pembacaan data dari file teks.
4. Penanganan data kosong dan data tidak valid.
5. Perhitungan rata-rata, nilai tertinggi, dan nilai terendah.
6. Penanganan file yang tidak ditemukan.
7. Penyimpanan hasil rekap ke file keluaran.

Pengujian dinyatakan berhasil apabila hasil aktual sesuai dengan hasil yang diharapkan pada setiap test case.

## 9. Analisis Efisiensi

Misalkan terdapat `n` data siswa.

- **Kompleksitas waktu:** O(n), karena program perlu membaca dan memproses setiap data siswa. Perhitungan statistik dan pengelompokan juga memerlukan waktu yang sebanding dengan jumlah siswa.
- **Kompleksitas ruang:** O(n), karena data siswa dan daftar hasil analisis disimpan dalam memori.

Efisiensi program cukup baik untuk mengolah data nilai kelas dengan ukuran kecil hingga menengah.

## 10. Kesimpulan

Program Rekap dan Analisis Nilai Matematika Kelas membantu mengotomatisasi proses pengolahan nilai siswa. Dengan memanfaatkan fungsi Python, pembacaan file, validasi data, dan perhitungan statistik, proses rekapitulasi dapat dilakukan secara lebih terstruktur dan konsisten.

Program ini juga dapat dikembangkan lebih lanjut dengan fitur pencarian siswa, pengurutan nilai, antarmuka pengguna, serta ekspor laporan ke format CSV atau Excel.