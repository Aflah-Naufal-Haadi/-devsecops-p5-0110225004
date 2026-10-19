
# Aplikasi Pengelolaan Tugas Sederhana

Aplikasi ini dibuat menggunakan Python untuk membantu mencatat dan mengelola tugas supaya lebih mudah dipantau.

## Fitur yang Tersedia
- Menambahkan tugas baru.
- Melihat daftar tugas yang sudah dicatat.
- Menandai tugas yang sudah selesai.
- Melihat jumlah tugas, baik yang sudah selesai maupun yang belum.

## Cara Menjalankan
1. Pastikan Python sudah terpasang di komputer/laptop.
2. Buka terminal pada folder proyek.
3. Jalankan perintah berikut:

   `python main.py`

## Teknologi yang Digunakan
- Python untuk membuat aplikasi.
- GitHub untuk menyimpan kode proyek.
- GitHub Actions untuk menjalankan pemeriksaan kode secara otomatis.


## Gambaran Pipeline CI/CD

Proyek ini menggunakan GitHub Actions untuk menjalankan pemeriksaan otomatis setiap ada push atau pull request ke branch main.

Pipeline terdiri dari tiga tahap:

1. Build dan pengujian: memeriksa sintaks Python dan menjalankan empat pengujian otomatis.
2. Pemindaian keamanan: menggunakan Bandit untuk memeriksa potensi masalah keamanan pada kode.
3. Quality Gate: memastikan tahap build dan pemindaian keamanan berhasil sebelum pipeline dinyatakan lulus.

