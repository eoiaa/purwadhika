README - Raditmart - Minimarket
Selamat datang di Raditmart, sebuah aplikasi berbasis Python untuk mengelola minimarket. Aplikasi ini dilengkapi dengan berbagai fitur seperti melihat daftar produk, menambahkan produk, memperbarui produk, menghapus produk, serta fitur pembelian produk.

Fitur Utama
Melihat List Produk:

Menampilkan semua produk yang tersedia di minimarket.
Memungkinkan pencarian produk berdasarkan nama, kategori, atau produsen.
Tambah Produk (Akses Admin):

Menambahkan produk baru ke daftar barang.
Pastikan untuk memasukkan detail seperti nama produk, kategori, harga, stok, dan produsen.
Memperbarui Produk (Akses Admin):

Mengedit detail produk seperti nama, kategori, harga, stok, atau produsen.
Mendukung pembaruan pada satu atau beberapa kolom sekaligus.
Menghapus Produk (Akses Admin):

Menghapus produk tertentu dari daftar barang.
Membeli Produk:

Memilih dan membeli produk dari daftar barang yang tersedia.
Mendukung pengurangan stok otomatis sesuai jumlah produk yang dibeli.
Menampilkan keranjang belanja secara real-time.
Keamanan Admin:

Untuk menambah, memperbarui, atau menghapus produk, pengguna harus memasukkan password admin (Admin#1234).
Cara Menjalankan Program
Persiapan:

Pastikan Anda telah menginstal Python di perangkat Anda (versi 3.6 atau lebih baru).
Simpan file program dengan nama raditmart.py.
Menjalankan Program:

Buka terminal atau command prompt.
Jalankan program dengan perintah:
bash
Copy code
python raditmart.py
Navigasi Menu:

Ikuti instruksi di layar untuk memilih menu dan submenu yang diinginkan.
Gunakan angka untuk memilih opsi pada menu.
Struktur Data
Program menggunakan struktur data berbasis dictionary untuk menyimpan informasi produk, dengan format berikut:

python
Copy code
barang = {
"nama": [<list_nama_produk>],
"kategori": [<list_kategori_produk>],
"harga": [<list_harga_produk>],
"stock": [<list_stok_produk>],
"produsen": [<list_produsen_produk>]
}
Panduan Fitur

1. Melihat List Produk
   Sub Menu:
   Melihat Semua Barang: Menampilkan semua produk dalam bentuk tabel.
   Cari Barang: Mencari produk berdasarkan nama, kategori, atau produsen.
2. Menambah Produk (Admin)
   Masukkan password admin: Admin#1234.
   Inputkan detail produk baru (nama, kategori, harga, stok, produsen).
   Produk tidak boleh memiliki nama yang sama dengan produk yang sudah ada.
3. Memperbarui Produk (Admin)
   Masukkan password admin: Admin#1234.
   Pilih produk yang ingin diperbarui, kemudian tentukan kolom yang ingin diubah.
4. Menghapus Produk (Admin)
   Masukkan password admin: Admin#1234.
   Pilih produk yang ingin dihapus dari daftar.
5. Membeli Produk
   Pilih produk dari daftar.
   Tentukan jumlah produk yang ingin dibeli.
   Stok produk akan berkurang secara otomatis setelah pembelian.
   Program akan menghitung total belanja, meminta pembayaran, dan memberikan kembalian jika diperlukan.
   Contoh Output
   Melihat Daftar Produk
   plaintext
   Copy code
   +----+--------------------+-----------+-------+-------+------------+
   | | nama | kategori | harga | stock | produsen |
   +====+====================+===========+=======+=======+============+
   | 0 | Susu UHT Fullcream | Minuman | 12000 | 20 | PT. Mayora |
   | 1 | Roti Tawar | Makanan | 15000 | 10 | Indofood |
   | 2 | Pasta Gigi | Kebutuhan | 8000 | 30 | Unilever |
   | 3 | Teh Botol | Minuman | 5000 | 50 | Dadone |
   | 4 | Mie Instan | Makanan | 3500 | 100 | Indofood |
   | 5 | Wawa | Makanan | 20000 | 0 | Kuala |
   +----+--------------------+-----------+-------+-------+------------+
   Membeli Produk
   plaintext
   Copy code
   Keranjang Belanja Anda:
   No Nama Produk Harga per Item Jumlah Harga Total  
   ====================================================================
   1 Mie Instan 3500 3 10500
   2 Teh Botol 5000 5 25000
   ====================================================================
   Total yang harus dibayar: Rp. 35500
   Masukkan jumlah uang: 50000
   Uang kembalian anda: 14500
   Terima kasih telah berbelanja di Raditmart 😘
   Catatan
   Password Admin: Admin#1234 digunakan untuk menambah, memperbarui, dan menghapus produk.
   Validasi Input: Program memeriksa semua input untuk memastikan data yang dimasukkan valid.
   Keranjang Belanja: Menyimpan produk yang dipilih hingga proses pembayaran selesai.
   Terima kasih telah menggunakan Raditmart! 😊
