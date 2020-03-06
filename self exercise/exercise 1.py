#personal information
# nama = ('Jihar Gifari')
# usia = (22)
# alamat = ('Jl. Sultan Agung No. 1 Bogor')
# print(nama, str(usia), alamat, sep = '\n')

#Sales Prediction
# profit_percentage = (23/100)
# total_sales = int(input("How much is your total sales? "))
# profit = str(total_sales*profit_percentage)
# print("Your profit is:  "+ profit)

# z = ''

# for i in range(5):
#     for j in range(i+1):
#         z += ' * '
#     z += '\n'    
    

# print(z)    

# x=4
# y=3
# z=2
# w=((x+y*z)/x*y)**z 
# print(w)

# inputan = int(input("silahkan masukkan angka berpapun: "))
# hasil = inputan**2
# print(hasil)

# jumlah_hari = int(input('jumlah hari: '))
# hasil_bulan = (jumlah_hari//30)
# hasil_minggu = (jumlah_hari-(hasil_bulan*30))//7
# hasil_hari = (jumlah_hari-(hasil_bulan*30))//1
# print("{} hari setara dengan {} Bulan {} Minggu dan {} hari".format(jumlah_hari, hasil_bulan, hasil_minggu, hasil_hari))

# total_umur = int(input("Masukkan total umur Andi dan Budi: "))
# rasio_umur = float(input("Masukkan rasio umur Andi dan Budi: "))
# tahun = int(input("mau menghitung umur Andi dan Budi berapa tahun dari sekarang? "))
# umurBudi = (total_umur*10)/(10+(rasio_umur*10))
# umurAndi = total_umur - umurBudi
# print("umur Budi dan Andi dua tahun dari sekarang adalah {} dan {}".format(umurBudi+tahun, umurAndi+tahun))

# kata = input("Masukkan kata-kata nya: ")
# cari = input("Masukkan karakter yang dicari: ")
# jumlah_karakter = (len(kata.split(cari))-1)
# print("kalimat'{}' memiliki huruf '{}' sebanyak {} huruf".format(kata, cari, jumlah_karakter))

# total_jarak = int(input("masukkan total jarak(km): "))
# kecepatan_A = int(input("masukkan kecepatan A(km/jam): "))
# kecepatan_B = int(input("masukkan kecepatan B(km/jam): "))
# total_kecepatan = kecepatan_A + kecepatan_B
# total_waktu = total_jarak/total_kecepatan
# jam = int((total_waktu*60)//60)
# menit = int(((total_waktu*60)-60)//1)
# jam_berangkat = int(input("masukkan jam berangkat: "))
# jam_tabrakan = jam_berangkat + jam
# jam_tabrakan_bener = "A dan B akan bertabrakan pukul {} lewat {} menit".format(jam_tabrakan, menit)
# print(jam_tabrakan_bener)

# numbers = int(input("insert four digit number: "))
# first_two = str(numbers//100)
# second_two = str(numbers%100)
# rotated_numbers = second_two+first_two
# print(rotated_numbers)

# import math
# radius = int(input("insert radius: "))
# area = (math.pi)*(radius**2)
# print("the area of the circle with radius {} is {}".format(radius, area))
# input1 = int(input("insert the first two digit number: "))
# input2 = int(input("insert the second two digit number: "))
# print(str(input1//10) + str(input2//10) + str(input1%10) + str(input2%10))

# words = input("insert words: ")
# character = input('insert missing character: ')
# print(words.replace(character, "_"))

# two_words = input("insert two words: ")
# lists = two_words.split()
# print(lists[1] + " " + lists[0])
# x = 10
# y = 20
# def basic(): 
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
# basic()
# def intermediate():
#     print(x**y)
#     print(x%y)
#     print(x//y)
# intermediate()

# def namaku(nama):
#     print(nama + ' Susilo')
# namaku('Adi')
# namaku('Budi')
# namaku('Caca')
# namaku('Dedi')

# def jumlah(x,y):
#     z=x+y
#     return z
# print(jumlah(4,5))

# def kali(angka1 = 5, angka2 = 2) :
#     return angka1 * angka2
# print(kali(angka2=4))

# mantan = ['rik', 'lol', 'lia', 'lisa','del', 'lina', 'rosa']
# for i in mantan :
#     if (len(i)<4):
#         print(i)
#     else :
#         print('-')
# mantan.append('adel')
# mantan.pop()
# print(mantan)

# listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
# print(listTest[1])
# print(listTest[:2])
# print(listTest[2])
# print(listTest[2][1:])
# print(listTest[2][2])
# print(listTest[2][3][0])

# angka = 1
# while angka < 20:
#     print(angka)
#     angka += 1

# listItem = list(range(1,11,2))
# print(listItem)

# for item in range(1,11,2):
#     print(item)
# y = 'Nomor Urut ' 
# x = 'urutan ke-'
# for item in range(1,11,1):
#     print(y + str(item))
    
# for item in range(1,11,1):
#     print(x + str(item))

# y = "Nomor urut "
# # for i in range(0,21,2):
# #     print(y + str(i))

# for i in range(1,20, 2):
#     print(y + str(i))

# z = ''
# for i in range(5, 0, -1):
#     for k in range(i):
#         z += ' * '
#     z += '\n'
# for i in range(1, 5, 1):
#     for k in range(i+1):
#         z += ' * '
#     z += '\n'
# print(z)

# z = ''
# for i in range(0, 11, 1):
#     for k in range(21):
#         if k >= 10-i and k<= 10+i:
#             z+=' * '
#         else : 
#             z+='   '
#     z+="\n"
# for i in range(10, -1, -1):
#     for k in range(21):
#         if k >= 10-i and k<= 10+i:
#             z+=' * '
#         else : 
#             z+='   '
#     z+="\n"
# print(z)

# arr = [5, 3, 2, 5, 78, 90, 23]
# def ascending(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j] :
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
# def descending(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j] :
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
# print(ascending(arr))
# print(descending(arr))
# angka_terendah = ascending(arr)[0]
# angka_tertinggi = descending(arr)[0] 
# print("angka tertinggi adalah {} dan angka terendah adalah {}".format(angka_tertinggi, angka_terendah))

# massa = int(input("masukkan massa(kg): "))
# tinggi = int(input("masukkan tinggi(cm): "))
# IMT = float(massa/(tinggi/100)**2)
# print("Massa {} kg & tinggi {} m \nIMT = {}".format(massa, tinggi/100, IMT))
# if IMT < 18.5 :
#     print("berat anda kurang")
# elif 18.5 < IMT < 24.9 :
#     print("berat anda ideal")
# elif 25.0 < IMT < 29.9 :
#     print("berat anda berlebih")
# elif 30.0 < IMT < 39.9 :
#     print("berat anda sangat berlebih")
# elif IMT > 39.9 :
#     print("anda tergolong OBESITAS")
# else :
#     print('Invalid Input')

# numList = [1,2,3]
# input = 'x'
# check1 = input in numList
# check2 = 'x' in ['x','y','z']
# check3 = 'ka' in 'kurakas'
# chek5 =  in numList
# print(check1)
# print(check2)
# print(check3)  
# print(chek5)

# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"] }
# c= { "key1" : { "key2" : "item2"}, "kucing" : [3, "jerapah"] }
# print(c["key1"], d["key1"])
# print(c["kucing"][1])

# t = (1, [0, "test"], { "a1" : True })
# print(t[2]["a1"])
# print(t[1])

t = (1, [0, "test"], { "a1" : True }, (0,{ "test" : 5 },2))
print(t[3][1]["test"])


kata = 'merdeka', 'helo', 'sohib', 'kari ayam'
search = input("search : ")
cari = search in kata
# for i in kata :
#     if search in kata == True :
#         print(i)
#     else :
#         print("lala")
print(cari)
     
