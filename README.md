# Studi-Kasus-4
    Nama_produk = {
    "nama": "Pop mie",
    "harga": "5000",
    "stok": "45"
    }
    print(Nama_produk)
  Pertama kita bikin struktur data nya terlebih dahulu atau biasa disebut dengan dictionary untuk menyimpan dan mengelola data


    while True:
       print ("MENU PENGOLALA DATA")
       print ("1. Tampilkan Seluruh Data")
       print ("2. Tambah Data Kategori")
       print ("3. Ubah Harga Produk")
       print ("4. Hapus Produk")
       print ("5. Keluar")
       pilihan = input("pilihan :")
  Setelah itu kita memakai pengulangan atau while loop untuk bikin atau menampilkan menu pengelola data nya, agar user dapat memilih pilihannya.
  outputnya :
  
    <img width="258" height="108" alt="WhatsApp Image 2026-09-15 at 21 15 42" src="https://github.com/user-attachments/assets/d698e6d4-4f3a-4e8e-aae1-11d0a5eaeeb8" />



    if pilihan == "1":
        print(Nama_produk)
Selanjutnya, jika user memilih pilihan yang pertama maka outputnya akan menampilkan data produk yang sudah kita bikin tadi.
  outputnya :
  
    <img width="381" height="139" alt="image" src="https://github.com/user-attachments/assets/fc91f051-c91e-4313-b00a-4423486a0185" />



     elif pilihan == "2":
        Nama_produk["Kategori Makanan"] = "makanan instan"
        print("setelah mengubah produk: ")
        print(Nama_produk)

Jika User memilih pilihan kedua maka outputnya akan menambahkan kategori baru kepada dictionary yang sudah dibuat.
outputnya :

     <img width="660" height="164" alt="image" src="https://github.com/user-attachments/assets/8fe6cb2a-da40-4aaa-b92b-ccedd0ce5168" />



      elif pilihan == "3":
        Nama_produk["harga"] = "8000"
        print("setelah mengubah harga:")
        print(Nama_produk)

Ketika user ingin mengubah harga, user tinggal memilih menu ketiga yang dimana akan mengubah harga produk di dictionary.
output : 

    <img width="647" height="165" alt="image" src="https://github.com/user-attachments/assets/9aa2e93c-2687-406b-b94d-8ba3b231e71f" />



       elif pilihan == "4":
        Nama_produk.pop("stok")
        print("setelah menghapus stok:")
        print(Nama_produk)
Jika user ingin menghapus stok di produk, user hanya tinggal memilih menu yang ke 4.
output :

     <img width="552" height="167" alt="image" src="https://github.com/user-attachments/assets/de8e3fd6-58e4-4ff0-9042-4f64c68fee90" />



       elif pilihan == "5":
        print("Keluar dari program:")
        break
Jika user ingin keluar dari menu pengelola data, user tinggal memilih menu yang 5.
output : 

      <img width="303" height="143" alt="image" src="https://github.com/user-attachments/assets/bfe717df-be0b-4072-8636-1aee581a729a" />

  
