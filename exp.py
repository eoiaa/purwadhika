def menu_utama():
    print("\nSelamat Datang di Raditmart - Minimarket")
    print("1. Melihat List Produk")
    print("2. Tambah Produk")
    print("3. Memperbarui Produk")
    print("4. Menghapus Produk")
    print("5. Membeli Produk")
    print("6. Keluar")

    while True:
        inputMenu = input("Masukkan angka menu yang ingin dijalankan: ")

        # Memeriksa apakah input adalah angka dan berada di antara 1 hingga 6
        if inputMenu.isdigit() and 1 <= int(inputMenu) <= 6:
            inputMenu = int(inputMenu)
            if inputMenu == 1:
                sub_menu_1()
            elif inputMenu == 6:
                print(
                    "Terima kasih telah menggunakan Raditmart - Minimarket. Sampai jumpa!")
                break
            else:
                print(f"Menu {
                      inputMenu} dipilih (logika untuk menu ini dapat ditambahkan sesuai kebutuhan)")
        else:
            print("Menu tidak tersedia, silakan masukkan angka 1 sampai 6.")


def sub_menu_1():
    print("\nSub Menu 1:")
    print("1. Melihat Semua Barang")
    print("2. Cek Barang")
    print("3. Kembali ke Menu Utama")

    while True:
        subMenuInput = input("Masukkan angka sub menu yang ingin dijalankan: ")

        # Memeriksa apakah input adalah angka dan berada di antara 1 hingga 3
        if subMenuInput.isdigit() and 1 <= int(subMenuInput) <= 3:
            subMenuInput = int(subMenuInput)
            if subMenuInput == 1:
                print("Menampilkan semua barang...")
            elif subMenuInput == 2:
                print("Memeriksa barang...")
            elif subMenuInput == 3:
                print("Kembali ke Menu Utama...\n")
                return  # Kembali ke menu utama
        else:
            print("Sub Menu tidak tersedia, silakan masukkan angka 1 sampai 3.")


# Memulai program dengan menampilkan Menu Utama
menu_utama()
