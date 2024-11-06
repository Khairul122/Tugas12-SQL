# Analisis Data Industri Kecamatan Kuala

Repository ini berisi kumpulan script Python untuk menganalisis dan memvisualisasikan data industri di Kecamatan Kuala. Setiap script menggunakan database MySQL 'pikm' untuk mengambil dan mengolah data dengan berbagai perspektif analisis.

## Persyaratan Sistem

- Python 3.x
- MySQL Server
- Library Python yang dibutuhkan:
  - pandas
  - matplotlib
  - mysql-connector-python

## Konfigurasi Database

Semua script menggunakan konfigurasi database yang sama:
```python
host: "localhost"
user: "root"
password: ""
database: "pikm"
```

## Deskripsi Script

### 1. Soal1.py - Analisis Distribusi KBLI
Script ini menganalisis distribusi jenis industri berdasarkan kode KBLI di Kecamatan Kuala.

Fitur:
- Mengambil data KBLI dan jumlah perusahaan
- Membuat visualisasi pie chart untuk distribusi industri
- Menampilkan legend dengan detail KBLI
- Menyajikan data dalam format tabel

Output:
- Pie chart distribusi jenis industri
- Tabel detail jumlah perusahaan per KBLI

### 2. Soal2.py - Analisis Pareto Nilai Investasi
Script ini membuat analisis Pareto untuk nilai investasi berdasarkan komoditi di Kecamatan Kuala.

Fitur:
- Menganalisis 12 jenis komoditi utama
- Menghitung persentase dan persentase kumulatif investasi
- Membuat diagram Pareto dengan dual axis

Output:
- Bar chart nilai investasi per komoditi
- Line chart persentase kumulatif
- Visualisasi gabungan dalam format diagram Pareto

### 3. Soal3.py - Analisis Industri Air Minum
Script ini fokus pada analisis khusus industri air minum di Kecamatan Kuala.

Fitur:
- Menganalisis data industri air minum dan air mineral
- Menghitung distribusi industri per kecamatan
- Membuat visualisasi Pareto chart

Output:
- Bar chart jumlah industri air minum
- Line chart persentase kumulatif
- Grid untuk memudahkan pembacaan data

### 4. Soal4.py - Perbandingan Nilai Investasi dan Produksi
Script ini membandingkan nilai investasi dan produksi untuk tiga perusahaan terpilih.

Fitur:
- Analisis tiga perusahaan: MENJAHIT SURYATI, USAHA PERABOT, dan USAHA BORDIR
- Visualisasi scatter plot dengan warna dan marker berbeda
- Anotasi nama perusahaan pada setiap titik data

Output:
- Scatter plot perbandingan nilai investasi vs produksi
- Legend dengan nama perusahaan
- Grid untuk memudahkan pembacaan data

## Cara Penggunaan

1. Pastikan semua persyaratan sistem terpenuhi
2. Import database 'pikm' ke MySQL server
3. Jalankan script yang diinginkan dengan perintah:
   ```bash
   python [nama_file].py
   ```
   Contoh: `python Soal1.py`

## Catatan Penting

- Pastikan koneksi database aktif sebelum menjalankan script
- Setiap script akan menutup koneksi database secara otomatis setelah selesai
- Hasil visualisasi akan ditampilkan menggunakan matplotlib viewer
- Data yang ditampilkan spesifik untuk Kecamatan Kuala

## Troubleshooting

Jika terjadi error, periksa:
1. Koneksi database (host, user, password)
2. Ketersediaan data di database
3. Instalasi library Python yang dibutuhkan

## Kontribusi

Untuk kontribusi atau pelaporan bug, silakan buat issue baru atau submit pull request.

Dosen : Subhan, ST, MSc.
Pertemuan : 12