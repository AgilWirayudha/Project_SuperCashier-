class Transaction:
    def __init__(self):
        '''
        Class Trasaction = untuk menyimpan metode yang akan digunakan, seperti memasukkan nama 
        barang, jumlah, dan harga barang.
        '''
        self.cart = {}
               
    def add_item(self, item_name, item_qty, item_price, last_item=False):
        '''
        Function untuk menambahkan barang ke dalam keranjang belanja
        
        args:
            item_name (str) = nama barang yang akan dimasukkan
            item_qty (int) = jumlah barang yang akan dimasukkan
            item_price (int) = harga barang yang akan dimasukkan
            last_item (bool) = apakah ini adalah item terakhir yang ditambahkan
        '''
        try:
            if item_qty <= 0 or item_price <= 0:
                raise ValueError ('Terdapat kesalahan penginputan, silakan coba kembali!')
            
            self.cart.update({item_name: [item_qty, item_price]})
            
            if last_item:
                print(f"Item yang dibeli adalah {self.cart}")
                
        except ValueError as e:
            print(e)
        except Exception as e:
            print('Terdapat kesalahan penginputan, silakan coba kembali!')
            
    def update_item_name(self, item_name, update_item_name):
        '''
        Function untuk mengganti nama barang apabila terdapat perubahan
        
        args:
            item_name (str) = nama barang yang akan diganti
            update_item_name (str) = nama barang baru
        '''
        try:
            if item_name in self.cart:
                self.cart[update_item_name] = self.cart.pop(item_name)
                print(f"Nama barang '{item_name}' telah diganti menjadi '{update_item_name}'")                
            else:
                print("Item yang Anda masukkan tidak ada di dalam keranjang")
        except Exception as e:
            print(e)
                       
    def update_item_qty (self, item_name, update_item_qty):
        '''
        Function untuk mengganti jumlah barang apabila terdapat perubahan
        
        args:
            item_name (str) = nama barang yang akan diganti
            update_item_qty (int) = jumlah barang baru
        '''
        try:
            if item_name in self.cart:
                self.cart[item_name][0] = update_item_qty
                print(f"Jumlah barang '{item_name}' telah diubah menjadi {update_item_qty}")
            else:
                print(f"'{item_name}' tidak ada dalam keranjang")
        except ValueError:
            print('Inputan salah, masukkan dengan angka')
        except Exception as e:
            print(e)
        
    def update_item_price(self, item_name, update_item_price):
        try:
            if item_name in self.cart:
                if update_item_price <= 0:
                    raise ValueError('Harga barang harus lebih dari 0!')
                    self.cart[item_name][1] = update_item_price
                print(f"Harga barang '{item_name}' telah diubah menjadi {update_item_price}")
            else:
                print(f"'{item_name}' tidak ada dalam keranjang")
        except ValueError as e:
            print(e)
        except Exception as e:
            print('Terjadi kesalahan, silakan coba kembali!')
            
    def delete_item(self, item_name):
        '''
        Adalah fungsi untuk menghapus barang yang sudah ada di keranjang belanja customer
        
        args:
            item_name (str) = nama barang yang akan dihapus
        '''
        try:
            if item_name in self.cart:
                self.cart.pop(item_name)
                print(f"Barang '{item_name}' telah dihapus dari keranjang")
            else:
                print(f"'{item_name}' tidak ada dalam keranjang")
        except Exception as e:
            print(e)

    def reset_transaction(self):
        '''
        Adalah fungsi untuk menghapu semua daftar barang belanjaan.
        '''
        try:
            self.cart = {}
            print('Semua item berhasil di-delete!')
        except Exception as e:
            print(e)
        
    def check_order(self):
        '''
        Adalah fungsi untuk memastikan barang belanjaan sudah tepat
        '''
        try:
            for item_name, item_data in self.cart.items():
                item_qty, item_price = item_data
                if not (isinstance(item_name, str) and isinstance(item_qty, int) and isinstance(item_price, int)):
                    raise ValueError("Terdapat kesalahan input pesanan")
                    print("Pemesanan sudah benar")
        except ValueError as e:
            print(e)
        except Exception as e:
            print('Terdapat kesalahan penginputan, silakan coba kembali!')

    def total_price(self):
        '''
        Function untuk menghitung total belanja berdasarkan keranjang belanja customer
        '''
        try:
            total_price = 0
            for item_data in self.cart.values():
                item_qty, item_price = item_data
                total_price += (item_qty * item_price)

            if total_price > 500_000:
                discount_percentage = 10
            elif total_price > 300_000:
                discount_percentage = 8
            elif total_price > 200_000:
                discount_percentage = 5
            else:
                discount_percentage = 0

            discount_amount = (total_price * discount_percentage) / 100
            discounted_total_price = total_price - discount_amount

            print(f'Item yang dibeli adalah {self.cart}.')
            if discount_percentage > 0:
                print(f'Anda mendapatkan diskon {discount_percentage}%, total yang harus Anda bayar adalah sebesar Rp {discounted_total_price}')
            else:
                print(f'Total yang harus Anda bayar adalah sebesar Rp. {total_price}')
        except Exception as e:
            print(e)