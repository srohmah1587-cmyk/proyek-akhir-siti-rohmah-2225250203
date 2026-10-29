# PROPOSAL PROYEK
# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

**Disusun oleh:**  
Nama: Siti Rohmah  
NIM: 2225250203  
Kelas: 3A  

**Mata Kuliah:** Algoritma dan Pemrograman

---

## 1. Latar Belakang

Matematika merupakan salah satu mata pelajaran yang berperan penting dalam mengembangkan kemampuan berpikir logis, kritis, sistematis, dan analitis siswa. Dalam proses pembelajaran matematika, penilaian dilakukan untuk mengetahui tingkat pemahaman siswa terhadap materi yang telah dipelajari. Hasil penilaian tersebut dapat digunakan oleh guru untuk mengevaluasi proses pembelajaran dan menentukan langkah perbaikan yang diperlukan.

Pengolahan nilai matematika dalam suatu kelas memerlukan ketelitian, terutama ketika jumlah siswa cukup banyak. Guru perlu melakukan pencatatan nilai, menghitung rata-rata kelas, mengidentifikasi nilai tertinggi dan terendah, serta menentukan jumlah siswa yang mencapai kriteria ketuntasan. Apabila seluruh proses dilakukan secara manual, kegiatan tersebut dapat membutuhkan waktu yang cukup lama dan berisiko menimbulkan kesalahan perhitungan.

Berdasarkan permasalahan tersebut, diperlukan sebuah program sederhana yang dapat membantu proses rekapitulasi dan analisis nilai matematika kelas secara lebih sistematis. Program ini dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan konsep dasar algoritma dan pemrograman, seperti variabel, percabangan, perulangan, fungsi, pengolahan file, validasi data, dan penanganan kesalahan.

Melalui program ini, data nilai matematika siswa diharapkan dapat diolah menjadi informasi yang lebih mudah dipahami. Informasi tersebut dapat membantu pengguna memperoleh gambaran umum mengenai hasil belajar siswa dalam satu kelas.

## 2. Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam proyek ini adalah sebagai berikut.

1. Bagaimana merancang program untuk membaca dan mengolah data nilai matematika siswa dalam satu kelas?
2. Bagaimana menerapkan validasi data untuk menghindari kesalahan dalam proses pengolahan nilai?
3. Bagaimana menghitung rata-rata kelas, nilai tertinggi, dan nilai terendah secara otomatis?
4. Bagaimana menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan batas nilai yang ditetapkan?
5. Bagaimana menerapkan proses debugging dan pengujian untuk memastikan program berjalan sesuai dengan kebutuhan?

## 3. Tujuan Proyek

Tujuan dari pengembangan program ini adalah:

1. Mengembangkan program rekapitulasi dan analisis nilai matematika kelas menggunakan Python.
2. Mempermudah proses pengolahan data nilai siswa secara otomatis.
3. Menghasilkan informasi statistik sederhana berupa rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan batas nilai yang telah ditentukan.
5. Menerapkan validasi data dan penanganan kesalahan dalam program.
6. Meningkatkan pemahaman mengenai penerapan konsep algoritma dan pemrograman dalam permasalahan pendidikan.

## 4. Manfaat Proyek

Proyek ini diharapkan memberikan manfaat sebagai berikut.

### 4.1 Bagi Guru

Program dapat membantu guru dalam melakukan rekapitulasi nilai matematika dan memperoleh gambaran umum mengenai hasil belajar siswa dalam satu kelas.

### 4.2 Bagi Siswa

Program dapat menjadi contoh penerapan teknologi dalam bidang pendidikan serta meningkatkan pemahaman mengenai pentingnya pengolahan data dalam proses evaluasi pembelajaran.

### 4.3 Bagi Pengembang

Proyek ini menjadi sarana untuk meningkatkan keterampilan pemrograman Python, khususnya dalam penggunaan fungsi, percabangan, perulangan, pengolahan file, validasi data, dan debugging.

### 4.4 Bagi Pembelajaran

Program dapat digunakan sebagai bentuk penerapan konsep algoritma dan pemrograman untuk menyelesaikan permasalahan sederhana yang berkaitan dengan kegiatan akademik.

## 5. Batasan Masalah

Agar pengembangan program lebih terarah, batasan masalah ditetapkan sebagai berikut.

1. Program dikembangkan menggunakan bahasa pemrograman Python.
2. Data siswa dibaca dari file teks bernama `nilai.txt`.
3. Setiap baris data memuat identitas siswa berupa NIM atau kode siswa dan nilai matematika, dengan format `NIM,nilai`.
4. Nilai yang diterima harus berupa angka dalam rentang 0 sampai 100.
5. Batas ketuntasan ditetapkan sebesar 60 untuk keperluan pengujian program dan dapat disesuaikan dengan ketentuan pembelajaran yang berlaku.
6. Program menghitung jumlah data siswa yang valid, rata-rata nilai kelas, nilai tertinggi, nilai terendah, jumlah siswa yang tuntas, dan jumlah siswa yang belum tuntas.
7. Data dengan format tidak sesuai atau nilai tidak valid akan dilewati dan diberikan peringatan.
8. Program menangani kondisi ketika file tidak ditemukan atau tidak terdapat data nilai yang valid.
9. Analisis yang dilakukan terbatas pada statistik deskriptif sederhana dan tidak digunakan sebagai satu-satunya dasar untuk menentukan kemampuan matematika siswa secara menyeluruh.

## 6. Metode Pelaksanaan

Pelaksanaan proyek dilakukan melalui beberapa tahapan berikut.

### 6.1 Analisis Kebutuhan

Tahap ini dilakukan dengan mengidentifikasi permasalahan dalam proses rekapitulasi nilai matematika kelas. Kebutuhan program meliputi data masukan, proses pengolahan, hasil keluaran, dan penanganan kesalahan.

### 6.2 Perancangan Algoritma

Pada tahap ini disusun langkah-langkah penyelesaian masalah, mulai dari membaca file, memvalidasi data, mengumpulkan nilai yang valid, menghitung statistik, hingga menentukan status ketuntasan siswa.

### 6.3 Implementasi Program

Algoritma yang telah dirancang kemudian diterapkan dalam kode Python. Program disusun menggunakan fungsi agar setiap proses dapat dikelola secara terstruktur dan mudah diperbaiki apabila ditemukan kesalahan.

### 6.4 Pengujian dan Debugging

Pengujian dilakukan menggunakan beberapa kondisi data, seperti data valid, nilai bukan angka, baris kosong, nilai di luar rentang yang diperbolehkan, dan file yang tidak ditemukan. Debugging dilakukan untuk menemukan serta memperbaiki kesalahan logika maupun kesalahan teknis dalam program.

### 6.5 Evaluasi Program

Tahap evaluasi dilakukan dengan membandingkan hasil keluaran program dengan hasil perhitungan yang diharapkan. Program dinyatakan memenuhi kebutuhan dasar apabila dapat membaca data yang valid, mengabaikan data yang tidak valid dengan tepat, dan menghasilkan perhitungan yang benar.

## 7. Rancangan Sistem

### 7.1 Data Masukan

Data masukan berupa file `nilai.txt` yang berisi kode siswa dan nilai matematika. Contoh data yang digunakan adalah sebagai berikut.

```text
A001,85
A002,78
A003,92
A004,abc
A005,60
A006,50
```

Pada data tersebut, baris `A004,abc` digunakan untuk menguji kemampuan program dalam menangani nilai yang tidak berbentuk angka.

### 7.2 Proses Pengolahan Data

Program dirancang untuk melakukan beberapa proses berikut.

1. Membuka dan membaca file data nilai matematika.
2. Memeriksa format setiap baris data.
3. Memvalidasi identitas siswa dan nilai yang dimasukkan.
4. Menyimpan data yang memenuhi ketentuan.
5. Menghitung rata-rata nilai matematika kelas.
6. Menentukan nilai tertinggi dan nilai terendah.
7. Menghitung jumlah siswa yang mencapai batas ketuntasan.
8. Menghitung jumlah siswa yang belum mencapai batas ketuntasan.
9. Menampilkan hasil analisis dan peringatan apabila ditemukan data yang tidak valid.

### 7.3 Data Keluaran

Hasil keluaran berupa informasi rekapitulasi dan analisis nilai matematika kelas yang ditampilkan melalui terminal. Informasi tersebut mencakup jumlah siswa dengan data valid, rata-rata nilai kelas, nilai tertinggi, nilai terendah, jumlah siswa tuntas, dan jumlah siswa belum tuntas.

## 8. Contoh Analisis Data

Berdasarkan data contoh pada bagian sebelumnya, nilai `abc` tidak dapat diproses sebagai nilai numerik sehingga data tersebut dilewati. Dengan demikian, terdapat lima data nilai yang valid.

| Komponen analisis | Hasil |
|---|---:|
| Jumlah data valid | 5 siswa |
| Rata-rata nilai | 73,00 |
| Nilai tertinggi | 92 |
| Nilai terendah | 50 |
| Jumlah siswa tuntas (nilai ≥ 60) | 4 siswa |
| Jumlah siswa belum tuntas (nilai < 60) | 1 siswa |

Hasil tersebut menunjukkan bahwa rata-rata nilai matematika dari data valid adalah 73,00. Sebanyak empat siswa mencapai batas ketuntasan yang ditetapkan, sedangkan satu siswa belum mencapainya. Informasi ini memberikan gambaran awal mengenai hasil belajar kelas, tetapi belum cukup untuk menjelaskan penguasaan setiap materi matematika secara mendalam.

## 9. Struktur Direktori Proyek

Struktur direktori yang direncanakan untuk proyek ini adalah sebagai berikut.

```text
program-rekap-nilai-matematika/
├── data/
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── praktik/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   ├── kasus_03_file_nilai.py
│   └── praktik_4_debugging.py
├── README.md
├── proposal.md
└── .gitignore
```

File `nilai.txt` digunakan untuk menyimpan data masukan. File `hasil_rekap.txt` disiapkan sebagai tempat penyimpanan hasil analisis apabila fitur penulisan hasil ke file telah diterapkan. Folder `praktik` berisi kode program dan latihan pengujian.

## 10. Rencana Pengujian

| No. | Skenario pengujian | Hasil yang diharapkan |
|---|---|---|
| 1 | File berisi data valid | Data berhasil dibaca dan dianalisis |
| 2 | File tidak ditemukan | Program menampilkan pesan kesalahan |
| 3 | Nilai berupa teks, seperti `abc` | Data dilewati dan peringatan ditampilkan |
| 4 | Terdapat baris kosong | Baris kosong dilewati |
| 5 | Nilai di bawah 0 atau di atas 100 | Data ditolak |
| 6 | Nilai siswa tepat 60 | Siswa dinyatakan tuntas |
| 7 | Tidak ada data valid | Program menampilkan pesan bahwa data tidak tersedia |
| 8 | Seluruh data valid | Hasil statistik ditampilkan secara benar |

## 11. Jadwal Pelaksanaan

| No. | Kegiatan | Waktu pelaksanaan |
|---|---|---|
| 1 | Analisis kebutuhan dan perumusan masalah | Tahap pertama |
| 2 | Perancangan algoritma dan struktur program | Tahap kedua |
| 3 | Implementasi program menggunakan Python | Tahap ketiga |
| 4 | Pengujian dan debugging | Tahap keempat |
| 5 | Evaluasi dan penyusunan dokumentasi | Tahap kelima |

Jadwal tersebut merupakan rencana pelaksanaan yang dapat disesuaikan dengan waktu pengerjaan tugas.

## 12. Penutup

Program Rekap dan Analisis Nilai Matematika Kelas dirancang sebagai solusi sederhana untuk membantu proses pengolahan nilai siswa secara lebih sistematis. Program ini menerapkan konsep dasar algoritma dan pemrograman dalam kegiatan pendidikan, khususnya untuk membaca data, memvalidasi nilai, menghitung statistik, dan menentukan ketuntasan siswa berdasarkan batas yang ditetapkan.

Melalui pengembangan proyek ini, diharapkan proses rekapitulasi nilai menjadi lebih efisien dan hasil perhitungan dapat diperoleh secara konsisten. Proyek ini juga diharapkan dapat meningkatkan keterampilan pemrograman serta memberikan pemahaman mengenai pemanfaatan teknologi untuk mendukung evaluasi pembelajaran matematika.