class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, nama_baru, jurusan_baru):
        for m in self.data:
            if m.nim == nim:
                m.nama = nama_baru
                m.jurusan = jurusan_baru

    def cari_data(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def tampilkan_semua_data(self):
        return self.data
