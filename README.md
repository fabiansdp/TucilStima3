# Tugas Kecil 3 Strategi Algoritma IF2211
> Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Daftar Isi
* [Kontributor](#kontributor)
* [Penjelasan](#penjelasan)
* [Spesifikasi](#spesifikasi)
* [Cara Pengunaan](#cara_penggunaan)

## Kontributor
* Fabian Savero Diaz Pranoto (13519140)
* Fadel Ananda Dotty (13519146)

## Penjelasan
Algoritma A* (atau A star) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, diminta menentukan lintasan terpendek berdasarakan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan atau ujung jalan. Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara lainnya yang disediakan oleh Google Map.

## Spesifikasi
1. Program menerima input file graf (direpresentasikan sebagai matriks ketetanggaan berbobot), jumlah simpul minimal 8 buah.
2. Program dapat menampilkan peta melalui Google Maps.
3. Program menerima input simpul asal dan simpul tujuan.
4. Program dapat menampilkan lintasan terpendek beserta jaraknya antara simpul asal dan simpul tujuan.

## Requirements
1. Flask
## Cara Penggunaan
Sebaiknya menginstall flask pada virtual environment saja. Untuk membuat virtual environment sebagai berikut:
```bash
pip install virtualenv
python -m venv env
```
Untuk menyalakan virtual environment, dari directory utama proyek ini:
```bash
source env/Scripts/activate
```
Setelah itu baru dapat menginstall flask dengan command sebagai berikut:
```bash
pip install flask
```
Untuk mennyalakan program, masukkan command sebagai berikut:
```bash
export FLASK_APP=src/main.py
flask run
```
