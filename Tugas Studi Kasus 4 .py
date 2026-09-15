Nama_produk = {
    "nama": "Pop mie",
    "harga": "5000",
    "stok": "45"
}
print(Nama_produk)
while True:
    print ("MENU PENGOLALA DATA")
    print ("1. Tampilkan Seluruh Data")
    print ("2. Tambah Data Kategori")
    print ("3. Ubah Harga Produk")
    print ("4. Hapus Produk")
    print ("5. Keluar")
    pilihan = input("pilihan :")

    if pilihan == "1":
        print(Nama_produk)

    elif pilihan == "2":
        Nama_produk["Kategori Makanan"] = "makanan instan"
        print("setelah mengubah produk: ")
        print(Nama_produk)

    elif pilihan == "3":
        Nama_produk["harga"] = "8000"
        print("setelah mengubah harga:")
        print(Nama_produk)

    elif pilihan == "4":
        Nama_produk.pop("stok")
        print("setelah menghapus stok:")
        print(Nama_produk)

    elif pilihan == "5":
        print("Keluar dari program:")
        break