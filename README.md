# BIODATA 

NAMA  : ADINDA AULIA NABILA PUTRI

NIM   : 312410309

KELAS : TI.24.A.4


# Deskripsi 

program ini merupakan manajemen data mahasiswa yang dibangun menggunakan python. program ini memungkinkan pengguna untuk mengubah data, menghapus data, dan mencari data mahasiswa. 

# Fitur 

* Tambah data mahasiswa
* Ubah data mahasiswa
* Hapus data mahasiswa
* Cari data mahasiswa berdasarkan NIM
* Tampilkan semua data mahasiswa

# Struktur proyek 

  ![WhatsApp Image 2024-12-10 at 10 56 38_22a0eb95](https://github.com/user-attachments/assets/8951bc0e-b471-4175-97b1-8e7a608db77a)

# Deskripsi Kode 

1. data/Mahasiswa.py

   File ini berisi definisi kelas Mahasiswa yang memiliki atribut nama, nim, dan nilai. Selain itu, terdapat beberapa fungsi untuk mengelola data mahasiswa:

* tambah_mahasiswa(data_mahasiswa, mahasiswa): Menambahkan objek mahasiswa ke dalam daftar.
* ubah_mahasiswa(data_mahasiswa, nim, nilai_baru): Mengubah nilai mahasiswa berdasarkan NIM.
* hapus_mahasiswa(data_mahasiswa, nim): Menghapus mahasiswa dari daftar berdasarkan NIM.
* cari_mahasiswa(data_mahasiswa, nim): Mencari mahasiswa berdasarkan NIM.
tampilkan_semua_mahasiswa(data_mahasiswa): Menampilkan semua data mahasiswa.

2. view/input_from.py

   file ini berisi fungsi input_data_mahasiswa() yang digunakan untuk mengambil input dari pengguna untuk menambah data mahasiswa.

3. view/mahasiswa.py

   File ini berisi fungsi tampilkan_data_mahasiswa(mahasiswa) yang digunakan untuk menampilkan informasi mahasiswa.

4. main.py

   File ini adalah file utama yang menjalankan aplikasi. Di dalamnya terdapat fungsi load_data() untuk memuat data dari file JSON dan save_data(data) untuk menyimpan data ke file JSON. Fungsi main() mengatur menu interaksi dengan pengguna.

