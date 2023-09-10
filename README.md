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
### Class Transaction()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/72fbd897-cb10-48c8-9a50-08021fdbff89)

### def add_item()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/a73ae59d-30cb-4ddd-9400-a6a5ac67ca2f)

### def update_item_name()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/8bc16c4b-a662-4d7a-a5bd-0af2273b262e)

### def update_item_qty()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/1b52b648-59ca-42ff-8081-84b2b4d546ec)

### def update_item_price()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/8df3605a-1806-442f-9462-ee041ba774a4)

### def delete_item()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/6fcfa55f-85ae-4857-b372-339fba0f6d50)

### def reset_transaction()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/5a2a3a65-a729-46ba-9178-e0fd365a2196)

### def check_order()
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/4b24b1c7-9a56-41cc-bb13-312991fdd83a)

### def total_price
impr![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/2ff35c84-288b-4316-ad44-2748078a4738)

# Test Case
## Test 1:
Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut : - Nama Item : Ayam Goreng, Qty : 2, Harga : 20000 - Nama Item : Pasta Gigi, Qty : 3. Harga : 15000
### output:
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/6124f895-1c8c-4ea5-bc85-a1ae0c82c1ca)

## Test 2:
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. item yang dihapuskan adalah Pasta Gigi.
## output:
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/c85cb4ca-7f32-4f98-91b7-b913cfe7125e)

## Test 3
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_keranjang() untuk menghapus semua item yang sudah ditambahkan:
## output:
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/2626b199-39b8-4778-be6e-cb8e44e7db6a)

## Test 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.
## output: 
![image](https://github.com/AgilWirayudha/Project_SuperCashier-/assets/144359538/76d9ef20-c28b-44a7-b1da-ff26380c5732)

# Future Work
Terdapat beberapa hal yang masih dapat dikembangkan di masa mendatang, beberapa diantaranya yakni:
1. pengadaan database yang meliputi item-item apa yang tersedia
2. fitur pencatatan transaksi sehingga dapat mempermudah dalam mencatat detail setiap transaksi untuk tujuan audit maupun analisis penjualan
3.  fitur menambahkan voucher atau kupon tertentu untuk lebih dapat menarik customer 
