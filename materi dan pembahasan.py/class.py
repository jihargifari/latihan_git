# class classy :
#     my_class = 5
#     your_class = 'ga ada'
# contoh = classy()
# # print(contoh.my_class)
# # print(contoh.your_class)

# class manusia :
#     def __init__(self,name,age):
#         self.nama = name
#         self.umur = age
#     def salamKenal(self):
#         print("Nama saya adalah {}, saya berumur {}".format(self.nama, self.umur))
#         # return(self.age * len(self.nama)))
# manusia1 = manusia('Baron', 22)
# # print(manusia1.salamKenal)
# # manusia1.salamKenal(', nama kamu siapa?')
# # print(manusia1)
# # print(manusia1.nama)
# # print(manusia1.umur)
# # print(manusia1.__dict__)
# # print(manusia1.__dict__['nama'])
# class anak(manusia) :
#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.kelamin = gender

# Ne1 = anak('Ne1', 27, 'Pria')
# Ne1.salamKenal()

class bikinMenu:
    def __init__(self, name, menu, price):
        self.nama = name
        self.menu = menu
        self.harga = price
        self.history = []
    def GetMenu(self) :
        print('Menu Makanan: ')
        print('1. {} harganya adalah {}'.format(self.menu[0], self.harga[0]))
        print('2. {} harganya adalah {}'.format(self.menu[1], self.harga[1]))
        print('3. {} harganya adalah {}'.format(self.menu[2], self.harga[2]))
    def MenuPrice(self) :
        pilihan = int(input('Mau beli yang mana: '))
        if pilihan == 1:
            print('{} telah membeli {} seharga {}'.format(self.nama, self.menu[0], self.harga[0]))
        elif pilihan == 2 :
            print('{} telah membeli {} seharga {}'.format(self.nama, self.menu[1], self.harga[1]))
        elif pilihan == 3 :
            print('{} telah membeli {} seharga {}'.format(self.nama, self.menu[2], self.harga[2])) 
        else :
            print('Invalid Input')
    def get_history(self):
        if len(self.history):
            z = '{} telah membeli'.format(self.nama)


Paul=bikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000,2000,3000])

Paul.GetMenu()
Paul.MenuPrice()
# Paul.MenuPrice()
# Paul.MenuPrice()
# Paul.MenuPrice()
Paul.get_history()


# PR8 CLASS RAMAL
# MENU RAMALAN : 1) PEKERJAAN, 2) KESEHATAN, 3) PERCINTAAN, 4) KELUAR
# MASUKKAN PILIHAN
