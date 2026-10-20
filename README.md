# Pertemuan 10 - String dan Pengolahan Teks

Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
Jalankan program dengan perintah berikut di terminal:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

## Algoritma
1. Membaca input nama mahasiswa dan kode kelas.
2. Menghapus spasi berlebih pada awal dan akhir nama.
3. Mengubah nama menjadi format title case.
4. Memisahkan nama menjadi kata-kata untuk menghitung jumlah kata dan membuat inisial.
5. Mengubah kode kelas menjadi huruf kapital.
6. Mengganti spasi pada kode kelas dengan tanda hubung.
7. Menampilkan hasil normalisasi nama, kode kelas, jumlah kata, dan inisial.

## Test Case

| No. | Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana \| PMAT-A-2026 \| AH` | `Aan Hendrayana \| PMAT-A-2026 \| AH` | Berhasil |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah \| KELAS-B \| FM` | `Fathiyyah Muthmainnah \| KELAS-B \| FM` | Berhasil |
| 3 | `BUDI` | `pmtk 01` | `Budi \| PMTK-01 \| B` | `Budi \| PMTK-01 \| B` | Berhasil |
| 4 | `siti nur ais yah` | `kelas c` | `Siti Nur Ais Yah \| KELAS-C \| SNAY` | `Siti Nur Ais Yah \| KELAS-C \| SNAY` | Berhasil |

## Refleksi
Masalah teks yang ditemukan adalah penggunaan huruf besar dan kecil serta spasi yang tidak konsisten. Masalah tersebut diperbaiki menggunakan fungsi `strip()`, `title()`, `upper()`, `split()`, dan `join()` agar data menjadi lebih rapi dan konsisten.

## Struktur Fungsi
- `normalisasi_nama()` untuk membersihkan dan merapikan nama mahasiswa.
- `buat_inisial()` untuk mengambil huruf awal setiap kata nama.
- `normalisasi_kode()` untuk mengubah kode kelas menjadi huruf kapital dan memisahkan kata dengan tanda hubung.
