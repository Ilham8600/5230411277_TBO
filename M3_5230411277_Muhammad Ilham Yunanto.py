class Makanan:
    def _init_(self, makanan, harga):
        self.makanan = makanan
        self.harga = harga

    def tampil(self):
        return f"{self.makanan} harga= {self.harga}"

class Minuman:
    def _init_(self, minuman, harga):
        self.minuman = minuman
        self.harga = harga

    def tampil(self):
        return f"{self.minuman} harga= {self.harga}"

makan_list = []
minum_list = []

while True:
    print("\n==== Menu Utama ====")
    print("1. Lihat Daftar Menu Makanan")
    print("2. Lihat Daftar Menu Minuman")
    print("3. Menambahkan Menu")
    print("4. Exit")
    pilih_menu = input("Pilih Menu di Atas: ")

    if pilih_menu == "1":
        print("\nDaftar Menu Makanan:")
        print("Daftar Menu")
        print("1. Mi Goreng (Rp.10000)")
        print("2. Martabak (Rp.45000)")
        print("3. Nasi Padang (Rp.10000)")
        print("4. Ayam Geprek (Rp.15000)")
        print("5. Sushi (Rp.60000)")
        for makanan in makan_list:
            print(makanan.tampil())

    elif pilih_menu == "2":
        print("\nDaftar Menu Minuman:")
        print("1. Air Mineral (Rp.3000)")
        print("2. Es Teh (Rp.5000)")
        print("3. Es Jeruk (Rp.5000)")
        for minuman in minum_list:
            print(minuman.tampil())

    elif pilih_menu == "3":
        print("1. Tambahkan Menu Makanan")
        print("2. Tambahkan Menu Minuman")
        pilih = input("Pilih: ")

        if pilih == "1":
            nama_makanan = input("Masukkan Nama Makanan: ")
            harga_makanan = input("Masukkan Harga Makanan: ")
            makanan_baru = Makanan(nama_makanan, harga_makanan)
            makan_list.append(makanan_baru)
            print(f"{nama_makanan} berhasil ditambahkan ke menu makanan.")

        elif pilih == "2":
            nama_minuman = input("Masukkan Nama Minuman: ")
            harga_minuman = input("Masukkan Harga Minuman: ")
            minuman_baru = Minuman(nama_minuman, harga_minuman)
            minum_list.append(minuman_baru)
            print(f"{nama_minuman} berhasil ditambahkan ke menu minuman.")

    elif pilih_menu == "4":
        print("Keluar dari program.")
        break

    else:
        print("Tidak Valid")
