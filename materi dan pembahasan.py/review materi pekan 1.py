# # Ini function untuk ngeprint

# print('test')
# print('a123')
# print('hello world')

# nama = 'Andi'
# print(nama)

# usia = 22
# usia = 23
# print(usia)

# test = 45
# test = 'text'
# print(type(test))

# nama = input('What is your name?: ')
# # String ditambah stringJ
# print('nama saya adalah' * 2)


# usiaAndi = 40
# usiaBudi = 12
# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaAndi ** usiaBudi)
# #Floor Division
# print(usiaAndi // usiaBudi) 

# # # Cara 1, inputan tetap string tapi di dalam printan dijadikan integer 
# # # baru jadi string lagi
# nama = input('Masukkan Nama: ')
# umur = input('Masukkan Umur: ')
# print('Umur saya 5 tahun kedepan adalah: ' + str(int(umur)+5))
# print('Umur saya adalah: ' +str(int(umur)//7) + ' Pekan')

# # # Cara 2, inputan dijadikan Integer terlebih dahulu
# # nama = input('Masukkan Nama: ')
# # umur = int(input('Masukkan Umur: '))
# # print('Umur saya 5 tahun kedepan adalah: ' +str(umur+5))
# # print('Umur saya jika di modulus 2 adalah: ' +str(umur%2))

# usiaAndi = 40
# usiaBudi = 20
# usiaAndi /= 3
# #UsiaAndi = usiaAndi + 3
# # usiaBudi -= 4
# #usiaBudi = usiaBudi * 4
# print(usiaAndi)
# print(usiaBudi)

import math

# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(8,2))
# print(math.sqrt(64))

# #Jika angka sebelum decimal adalah ganjil, maka pembulatan ke atas 
# # kalau genap maka ke bawah (dalam kasus .5)

# print(round(5.523456789876543, 0))
# print(round(3.4))


# print(math.floor(4.7))
# print(math.ceil(4.4))


# x = 'Halo Dunia'
# print(len(x))
# print(x.index('a'))
# print(x.split())
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.replace('Dunia', 'Apa'))


# Kita juga bisa melakukan index terbalik dengan cara menggunakan angka negatif di dalam index
# text = "I'm Baron Nice to meet you"
# print(text[1])
# print(text[2:])
# print(text[:6])
# print(text[2:5])
# print(text[-4:-1])
# print(text[::-1])



# # # # Soal latihan
# nama = input('Masukkan Nama: ').capitalize()
# umur = int(input('Masukkan Umur: '))

# print('Nama saya jika dimunculkan 2x: '+ nama*2 )

# print('Karakter di nama saya pada posisi modulus 2 umur saya: ' + nama[umur%2])

# print("""Karakter di nama saya pada posisi negatif modulus 2 umur saya lalu 
#         ditambah 5 hingga sebelum -1 adalah """ + nama[ (-1*(umur%2))-5 : -1])

#Homework

# No1
# x=4
# y=3
# z=2
# w = ((x+y*z)/(x*y))**z
# print(w)


# #No2
# angka = int(input("Silahkan masukkan angka berapapun: "))
# print("Kuadrat dari "+ str(angka) + " = " + str(angka**2))

# No3 (total hari dijadikan satu - satu ke tahun, bulan, etc.)
# CARA GUE
# jumlah_hari = int(input('Masukkan jumlah hari : '))
# tahun = 360
# bulan = 30
# pekan = 7
# hari = 1
# tahun1 = jumlah_hari//tahun
# bulan1 = (jumlah_hari%tahun)//bulan
# pekan1 = ((jumlah_hari%tahun)%bulan)//pekan
# hari1 = (((jumlah_hari%tahun)%bulan)%pekan)//hari
# print (str(tahun1) + ' tahun ' + str(bulan1) + ' bulan ' + str(pekan1) + ' pekan ' + str(hari1) + ' hari ')

# CARA BANG CORNELL
# import math
# total_hari1 = int(input("masukkan hari: "))
# tahun1 = str(math.floor(total_hari1/360))
# bulan1 = str(math.floor((total_hari1 % 360)/30))
# minggu1 = str(math.floor(((total_hari1 % 360)%30)/7))
# hari1 = str(math.floor(((total_hari1 % 360)%30)%7))
# print(tahun1 + " tahun " + bulan1 + " bulan " +  minggu1 + " minggu " + hari1 + " hari ")


# #No4
# total = int(input('Total umur Jihar dan Icin?: '))
# rasio = float(input('Rasio umur Jihar dan Icin?: '))

# umur_Jihar = (total * 10) /(10 + (rasio * 10))
# umur_icin = total - umur_Jihar
# print('Umur Jihar 2 tahun lagi adalah {}'.format(umur_Jihar + 2))
# print('Umur Icin 2 tahun lagi adalah {}'.format(umur_icin + 2))

# angka1 = int(input('Masukkan angka 1: '))
# angka2 = int(input('Masukan angka 2: '))
# print('Angka anda adalah {} dan {}'.format(angka1,angka2))


# print('Hlo Dunia'.split('a'))

# No5
# word = input('Kata: ')
# cari = input('Karakter yang ingin dicari: ')
# print(int(len(word.split(cari)))-1)

# # No6
# import math

# jarak_dalam_km = int(input("Jarak antara kendaraan?: "))
# kecepatan_a_km_per_h = int(input("Kecepatan kendaraan a?: "))
# kecepatan_b_km_per_h = int(input("Kecepatan kendaraan b?: "))
# jam_berangkat = int(input('Jam Berangkat?: '))
# menit_berangkat = int(input('Menit Berangkat?: '))

# waktu_tabrakan_dalam_menit = (
#     jarak_dalam_km/(kecepatan_a_km_per_h + kecepatan_b_km_per_h))*60
# print(str(waktu_tabrakan_dalam_menit) + ' menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

# print('Waktu A & B bertabrakan adalah jam {}.{} WIB'.format(int(jam), int(menit)))
# #jam 10.12 WIB


#PR Tambahan

# 1. Given a four-digit number, perform its cyclic rotation by two digits

# a = int(input('Masukkan Angka:'))
# print(a % 100 * 100 + a // 100)


# 2. Given a radius of the circle, calculate the area of the circle

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 3. Given two two-digit numbers, merge their digits as shown in the tests below.

# a = int(input('Masukkan 2 angka pertama: '))
# b = int(input('Masukkan 2 angka kedua: '))
# tens_a = a // 10
# units_a = a % 10
# tens_b = b // 10
# units_b = b % 10
# print(tens_a * 1000 + tens_b * 100 + units_a * 10 + units_b)


# 4. Given a string. Create a program to remove the character you want

# a = input('Masukkan Kata: ')
# rep = input('Kata yang dihilangkan: ')
# # rep2 = input('Kata yang dihilangkan: ')
# print(a.replace(rep, ''))
# # print(hilang.replace(rep2, ''))


# 5. Given a string consisting of exactly two words separated by a space. 
# Print a new string with the first and second word positions swapped (the second word is printed first).

# a = input('masukkan kata : ')
# lis = a.split()
# print(lis)
# print(lis[2] + ' ' + lis[1] +' '+ lis[0])


#Hw1

# z = ''
# for i in range(5, 0, -1):
    
#     for j in range (0, i):
#         z += ' 1 '
    
#     z += '\n'    
# print(z)    







#Hw2

# z = ''
# for i in range(5, 0, -1):
    
#     if (i > 1):
#         for j in range (0, i):
#             z += ' * '
#         z += '\n'
    
#     elif i == 1:
#         for k in range (0, 5):
#             for l in range (0 , k+1):
#                 z += ' * '
#             z += '\n'        
# print (z)    




# Hw3  
#      
# z= ''
# for i in range (0,10,1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
            



#Hw4
# z= ''
# for i in range (10,-1, -1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
# print (z)         
# 
# 
#       

#Hw5 Bintang Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (10,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)       

#Hw5 Bintang Tidak Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (11,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)     





# HW Bonus




size = int(input('Masukkan Besar Bintang: '))
z = ''
for j in range (size+1):
    if j < size:
        for k in range (1,size*2):
            if k <=size-j or k >= size+j:
                z += ' * '
            else:
                z += '   '
        z += '\n'            
    else:
        for l in range (size-2, -1, -1):
            for m in range (1,size*2):
                if m <=size-l or m >= size+l:
                    z += ' * '
                else:
                    z += '   '
            z += '\n'

print(z)