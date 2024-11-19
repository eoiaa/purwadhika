# Raditmart - Minimarket ss

from tabulate import tabulate

barang = {
    "nama": [
        "Susu UHT Fullcream",
        "Roti Tawar",
        "Pasta Gigi",
        "Teh Botol",
        "Mie Instan",
        "Wawa"
    ],
    "kategori": [
        "Minuman",
        "Makanan",
        "Kebutuhan",
        "Minuman",
        "Makanan",
        "Makanan"
    ],
    "harga": [
        12000,
        15000,
        8000,
        5000,
        3500,
        20000
    ],
    "stock": [
        20, 10, 30, 50, 100, 0
    ],
    "produsen": [
        "PT. Mayora",
        "Indofood",
        "Unilever",
        "Dadone",
        "Indofood",
        "Kuala"
    ]
}
total = 0


def menu():
    print(f"""
Selamat Datang di Raditmart - Minimarket
1. Melihat List Produk
2. Tambah Produk
3. Memperbarui produk
4. Menghapus Produk
5. Membeli Produk
6. Keluar
        """)


def subMenu1():
    print(f"""
Sub Menu 1 :
1. Melihat Semua barang
2. Cari Barang
3. Kembali ke Menu Utama
              """)


def subMenu2():
    print(f"""
Sub Menu 2 :
1. Tambah Produk
2. Kembali ke Menu Utama
              """)


def subMenu3():
    print(f"""
Sub Menu 3 :
1. Update Produk
2. Kembali ke Menu Utama
          """)


def subMenu4():
    print(f"""
Sub Menu 4 :
1. Hapus Produk
2. Kembali ke Menu Utama
          """)


def subMenu5():
    print(f"""
Sub Menu 5 :
1. Beli Produk
2. Kembali ke Menu Utama
          """)


def listProduk():
    print(tabulate(barang, headers=barang.keys(),
          tablefmt="rounded_grid", showindex="always"))


def minimarket():
    while True:
        menu()
        inputMenu = input("Masukkan angka menu yang ingin dijalankan: ")
        if inputMenu == "1":
            sub1()
        elif inputMenu == "2":
            while True:
                inputPass = input("Masukkan Password: ")
                if inputPass == "Admin#1234":
                    sub2()
                    break
                else:
                    print("Password Salah!")
        elif inputMenu == "3":
            while True:
                inputPass = input("Masukkan Password: ")
                if inputPass == "Admin#1234":
                    sub3()
                    break
                else:
                    print("Password Salah!")
        elif inputMenu == "4":
            while True:
                inputPass = input("Masukkan Password: ")
                if inputPass == "Admin#1234":
                    sub4()
                    break
                else:
                    print("Password Salah!")
        elif inputMenu == "5":
            sub5()
        elif inputMenu == "6":
            print(
                "Terima kasih telah Berbelanja di Raditmart. Sampai jumpa!")
            exit()
        else:
            print("Menu tidak tersedia!")


def sub1():
    while True:
        subMenu1()
        inputSubMenu1 = input("Masukkan angka pada Sub Menu: ")
        if inputSubMenu1 == "1":
            if not barang["nama"]:
                print("Produk tidak tersedia")
            else:
                listProduk()
        elif inputSubMenu1 == "2":
            inputPencarian = input("Masukkan Produk yang ingin dicari: ")
            hasil = []

            for i in range(len(barang["nama"])):
                if (
                    (inputPencarian.lower() in barang["nama"][i].lower()) or
                    (inputPencarian.lower() in barang["kategori"][i].lower()) or
                    (inputPencarian.lower()
                     in barang["produsen"][i].lower())
                ):
                    hasil.append({
                        "nama": barang["nama"][i],
                        "kategori": barang["kategori"][i],
                        "harga": barang["harga"][i],
                        "stock": barang["stock"][i],
                        "produsen": barang["produsen"][i]
                    })

            if not hasil:
                print("Produk tidak tersedia.")
            else:
                print(f"{'Nama': < 20} {'Kategori': < 10} {
                    'Harga (Rp)': < 10} {'Stok': < 5} {'Produsen': < 10}")
                print("="*60)
                for item in hasil:
                    print(f"{item['nama']: < 20} {item['kategori']: < 10} {
                          item['harga']: < 10} {item['stock']: < 5} {item['produsen']: < 10}")
        elif inputSubMenu1 == "3":
            menu()
            return
        else:
            print("Menu Tidak Tersedia!")


def sub2():
    while True:
        subMenu2()
        inputSubMenu2 = input("Masukkan angka pada Sub Menu: ")
        if inputSubMenu2 == "1":
            inputNama = input("Masukkan Nama Produk: ")
            while inputNama == "":
                print("Nama Produk tidak boleh kosong")
                inputNama = input("Masukkan Nama Produk: ")
            inputKategori = input("Masukkan Kategori Produk: ")
            while inputKategori == "":
                print("Kategori Produk tidak boleh kosong")
                inputKategori = input("Masukkan Kategori Produk: ")
            inputHarga = input("Masukkan Harga Produk: ")
            while not inputHarga.isdigit():
                print("Masukkan Angka!")
                inputHarga = input("Masukkan Harga Produk: ")
            else:
                inputHarga = int(inputHarga)
            inputStock = input("Masukkan Stock Produk: ")
            while not inputStock.isdigit():
                print("Masukkan Angka!")
                inputStock = input("Masukkan Stock Produk: ")
            else:
                inputStock = int(inputStock)
            inputProdusen = input("Masukkan Produsen dari Produk: ")
            while inputProdusen == "":
                print("Produsen tidak boleh kosong")
                inputProdusen = input("Masukkan Produsen dari Produk: ")

            if inputNama.lower() in [nama.lower() for nama in barang["nama"]]:
                print("Nama Produk sudah ada!")
            else:
                barang["nama"].append(inputNama)
                barang["kategori"].append(inputKategori)
                barang["harga"].append(int(inputHarga))
                barang["stock"].append(int(inputStock))
                barang["produsen"].append(inputProdusen)

                print(f"Produk berhasil ditambahkan")
        elif inputSubMenu2 == "2":
            menu()
            return
        else:
            print("Menu Tidak Tersedia!")


def sub3():
    listProduk()
    while True:
        subMenu3()
        inputSubMenu3 = input("Masukkan angka pada Sub Menu: ")
        if inputSubMenu3 == "1":
            while True:
                namaProduk = input(
                    "Masukkan Nama produk yang ingin di update: ").strip()

                if namaProduk.lower() == 'exit':
                    return

                if namaProduk.lower() in [nama.lower() for nama in barang["nama"]]:
                    index = next(i for i, nama in enumerate(
                        barang["nama"]) if nama.lower() == namaProduk.lower())
                    print("\nKolom: ")
                    print("1. Nama")
                    print("2. Kategori")
                    print("3. Harga")
                    print("4. Stock")
                    print("5. Produsen")
                    print("6. Update Semua Kolom")

                    pilih = input("Masukkan Kolom yang ingin di Update: ")
                    if pilih == "1":
                        barang["nama"][index] = input(
                            "Masukkan Nama baru: ").strip()
                        while barang["nama"][index] == "":
                            print("Nama produk harus diisi!")
                            barang["nama"][index] = input(
                                "Masukkan nama baru: ").strip()
                        break
                    elif pilih == "2":
                        barang["kategori"][index] = input(
                            "Masukkan Kategori baru: ").strip()
                        while barang["kategori"][index] == "":
                            print("Kategori produk harus diisi!")
                            barang["kategori"][index] = input(
                                "Masukkan Kategori baru: ").strip()
                        break
                    elif pilih == "3":
                        barang["harga"][index] = input(
                            "Masukkan harga baru: ").strip()
                        while not barang["harga"][index].isdigit():
                            print("Harga harus berupa angka!")
                            barang["harga"][index] = input(
                                "Masukkan harga baru: ").strip()
                        else:
                            barang["harga"][index] = int(
                                barang["harga"][index])
                        break
                    elif pilih == "4":
                        barang["stock"][index] = input(
                            "Masukkan stock baru: ").strip()
                        while not barang["stock"][index].isdigit():
                            print("Stock harus berupa angka!")
                            barang["stock"][index] = input(
                                "Masukkan stock baru: ").strip()
                        else:
                            barang["stock"][index] = int(
                                barang["stock"][index])
                        break
                    elif pilih == "5":
                        barang["produsen"][index] = input(
                            "Masukkan Produsen baru: ").strip()
                        while barang["produsen"][index] == "":
                            print("Produsen produk harus diisi!")
                            barang["produsen"][index] = input(
                                "Masukkan Produsen baru: ").strip()
                        break
                    elif pilih == "6":
                        # Nama
                        barang["nama"][index] = input(
                            "Masukkan Nama baru: ").strip()
                        while barang["nama"][index] == "":
                            print("Nama produk harus diisi!")
                            barang["nama"][index] = input(
                                "Masukkan nama baru: ").strip()

                        # Kategori
                        barang["kategori"][index] = input(
                            "Masukkan Kategori baru: ").strip()
                        while barang["kategori"][index] == "":
                            print("Kategori produk harus diisi!")
                            barang["kategori"][index] = input(
                                "Masukkan Kategori baru: ").strip()

                        # Harga
                        barang["harga"][index] = input(
                            "Masukkan harga baru: ").strip()
                        while not barang["harga"][index].isdigit():
                            print("Harga harus berupa angka!")
                            barang["harga"][index] = input(
                                "Masukkan harga baru: ").strip()
                        else:
                            barang["harga"][index] = int(
                                barang["harga"][index])

                        # Stock
                        barang["stock"][index] = input(
                            "Masukkan stock baru: ").strip()
                        while not barang["stock"][index].isdigit():
                            print("Stock harus berupa angka!")
                            barang["stock"][index] = input(
                                "Masukkan stock baru: ").strip()
                        else:
                            barang["stock"][index] = int(
                                barang["stock"][index])

                        # Produsen
                        barang["produsen"][index] = input(
                            "Masukkan Produsen baru: ").strip()
                        while barang["produsen"][index] == "":
                            print("Produsen produk harus diisi!")
                            barang["produsen"][index] = input(
                                "Masukkan Produsen baru: ").strip()

                        print(
                            f"Produk {barang["nama"][index]} berhasil di Diperbarui")
                        break
                else:
                    print(
                        "Produk tidak ditemukan! Pastikan nama produk sudah sesuai")
        elif inputSubMenu3 == "2":
            menu()
            return
        else:
            print("Menu Tidak Tersedia!")


def sub4():
    while True:
        subMenu4()
        inputSubMenu4 = input("Masukkan angka pada Sub Menu: ")
        if inputSubMenu4 == "1":
            listProduk()
            while True:
                inputHapus = input(
                    "Masukkan Nama Produk yang ingin dihapus: ").strip()
                if inputHapus.lower() in [nama.lower() for nama in barang["nama"]]:
                    index = next(i for i, nama in enumerate(
                        barang["nama"]) if nama.lower() == inputHapus.lower())
                    for j in barang:
                        del barang[j][index]
                    listProduk()
                    print(f"Data pada Produk {inputHapus} berhasil dihapus")
                    break
                else:
                    print(
                        f"Produk {inputHapus} tidak ditemukan! Pastikan nama produk sudah sesuai!")
        elif inputSubMenu4 == "2":
            menu()
            return
        else:
            print("Menu Tidak Tersedia!")


def showKeranjang(keranjang):
    print("\nKeranjang Belanja Anda:")
    print(f"{'Nama Produk':<20} {'Jumlah':<10} {'Harga Total':<15}")
    print("=" * 45)
    for item in keranjang:
        print(f"{item["nama"]:<20} {item["jumlah"]: < 10} {
              item["hargaTotal"]: < 15}")
    print("=" * 45)


def sub5():
    keranjang = []
    while True:
        subMenu5()
        inputSubMenu5 = input("Masukkan angka pada Sub Menu: ")
        if inputSubMenu5 == "1":
            while True:
                listProduk()
                inputBeli = input(
                    "Masukkan Nama Produk yang ingin dibeli: ").strip()

                if inputBeli.lower() not in [nama.lower() for nama in barang["nama"]]:
                    print(f"Produk {inputBeli} tidak Tersedia!")
                    continue

                index = next(i for i, nama in enumerate(
                    barang["nama"]) if nama.lower() == inputBeli.lower())

                if barang["stock"][index] == 0:
                    print(
                        f"Produk {barang['nama'][index]} sudah habis! Silahkan cari produk yang lain")
                    continue

                while True:
                    try:
                        inputJumlah = int(input(f"Masukkan jumlah {
                                          inputBeli} yang ingin dibeli(Stock: {barang['stock'][index]}): "))
                        if inputJumlah > barang['stock'][index]:
                            print(f"Stock {barang['nama'][index]} tinggal {
                                  barang['stock'][index]}!")
                        elif inputJumlah <= 0:
                            print("Jumlah Produk harus lebih dari 0!")
                        else:
                            break
                    except ValueError:
                        print("Input Jumlah harus berupa angka!")
                hargaTotal = barang["harga"][index] * inputJumlah
                keranjang.append({
                    "nama": inputBeli,
                    "jumlah": inputJumlah,
                    "hargaTotal": hargaTotal
                })
                barang["stock"][index] -= inputJumlah

                showKeranjang(keranjang)

                beliLagi = input("Apakah anda ingin belanja lagi? (y/t): ")
                if beliLagi == "t":
                    break

            total = sum(item["hargaTotal"] for item in keranjang)
            print(f"Total yang harus dibayar: Rp.{total} ")

            while True:
                try:
                    bayar = int(input("Masukkan jumlah uang: "))
                    if bayar > total:
                        print(f"Uang kembalian anda: {bayar - total}")
                        print("Terima kasih telah berbelanja di Raditmart 😘")
                        break
                    elif bayar < total:
                        print(f"Uang anda kurang: {total - bayar}")
                    else:
                        print("Terima kasih telah berbelanja di Raditmart 😘")
                        break
                except ValueError:
                    print("Uang harus berupa angka")
        elif inputSubMenu5 == "2":
            menu()
            return
        else:
            print("Menu Tidak Tersedia!")


minimarket()
