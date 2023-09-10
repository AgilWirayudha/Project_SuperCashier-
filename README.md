# Project Super Cashier

## Project Python - Agil Wirayudha - ADS

# Background
Seorang pemilik salah satu supermarket besar di salah satu kota di Indonesia yang membutuhkan sistem kasir yang dapat self-service di supermarket miliknya. Customer yang datang bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur lainnya. Pemilik tersebut membutuhkan programmer untuk membuatkan fitur-fitur tersebut agar bisa menerapkan sistem self-service di supermarket miliknya.

# Objective 
Membuat sistem kasir self-service agar customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur lainnya

# Requirement
1. Menambahkan item
2. Mengubah nama, jumlah dan harga dari item
3. Melakukan update detail produk
4. Menghapus item dari keranjang belanja
5. Menghapus seluruh item dari keranjang belanja
6. Melakukan pengecekan item apa saja yang ada di keranjang belanja
7. Menghitung total belanja beserta diskonnya (apabila ada)

# Flowchart

# Code Explanation
1. Class Transaction()
2. def add_item()
3. def update_item_name()
4. def update_item_qty()
5. def update_item_price()
6. def delete_item()
7. def reset_transaction()
8. def check_order()
9. def total_price

# Test Case
## Test 1:
Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut : - Nama Item : Ayam Goreng, Qty : 2, Harga : 20000 - Nama Item : Pasta Gigi, Qty : 3. Harga : 15000
### output:

## Test 2:
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. item yang dihapuskan adalah Pasta Gigi.
## output:

## Test 3
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_keranjang() untuk menghapus semua item yang sudah ditambahkan:
## output:

## Test 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.
## output:

# Future Work
Terdapat beberapa hal yang masih dapat dikembangkan di masa mendatang, beberapa diantaranya yakni:
1. pengadaan database yang meliputi item-item apa yang tersedia
2. fitur pencatatan transaksi sehingga dapat mempermudah dalam mencatat detail setiap transaksi untuk tujuan audit maupun analisis penjualan
3.  fitur menambahkan voucher atau kupon tertentu untuk lebih dapat menarik customer 
