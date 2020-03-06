# print('test')

# nama = 'jihar'
# print(nama)
# usia = 20
# usia = 22
# print(usia)

# jomblo = True
# print(jomblo)
# nama = 'andi'
# usia = 22
# jomblo = True

# print(type(nama))
# print(type(usia))
# print(type(jomblo))

# # nama = input("what is your name? : ")
# print("nama : " + nama) 
# print("umur : " + usia)
# print("apakah anda jomblo?" + jomblo)

# UsiaAndi = 40
# UsiaAndi += 3

# print(UsiaAndi)

# umur = int(input("umur saya berapa : "))
# print("umur saya lima tahun kedepan adalah : " + str((umur + 5)))

# usiaAndi = 40
# usiaBudi = 20
# usiaAndi += 3 
# #usiaAndi = usiaBudi + 3
# usiaBudi *= 4
# print(usiaAndi)
# print(usiaBudi)

# import math
# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(8, 2))
# print(math.sqrt(64))

# import math
# print(round(4.7))
# print(round(4.4))
# print(math.floor(4.7))
# print(math.ceil(4.4))
# print(round(5.34567898765, 2))

# import math
# import new
# print(new.value) 

# x = 'halo dunia'

# print(len(x))
# print(x.index('a'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# text = "i'm Baron, nice to meet you"

# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])
# print(text[11:15])
# print(text[::-1])

# nama = input("Masukkan nama: ").capitalize()
# umur = int (input("Masukkan umur: "))
# print("Nama saya jika dimunculkan 2x: "+ nama*2)
# print("Karakter di nama saya pada posisi modulus 2 umur saya: " + nama[umur%2])
# print("karakter di nama saya pada posisi negatif modulus 2 umur saya lalu ditambah hingga sebelum -1 adalah " + nama[ (-1*(umur%2))-5 : 1])

#solve2
# import math
# x = 4
# y = 3
# z = 2
# w = (math.pow(((x+(y*z))/(x*y)), z))
# print(w)

# angka = input("masukkan angka: ")
# print(angka)
# print(math.pow(int(angka), 2))

#solve3
# jumlah = 485
# tahun = 360
# bulan = 30
# minggu = 7
# hari = 1
# print = input(str((jumlah//tahun)) + ' Tahun')
# print = input(str((jumlah-tahun)//bulan) + ' Bulan') 
# print = input(str(((jumlah-tahun)-bulan*4)//minggu) + ' minggu')
# print = input(str(((jumlah-tahun)-(bulan*4)//hari)) + ' Hari')


#Solve4
# usiaBersama = 49
# usiaAndi = round(usiaBersama*0.4)
# usiaBudi = round(usiaBersama*0.6)
# usiaAndi += 2
# usiaBudi += 2
# print(usiaAndi)
# print(usiaBudi)


#Solve5
# x = "halo dunia"
# print("Halo dunia memiliki huruf 'a' sebanyak " + str(x.count('a')) + " buah")

#Solve6

# jarak = 120 
# tabrakan = ('jam ' + str(9 + jarak//(60+40))) + ':' + str(int((jarak%(60+40)/(60+40)*60)))
# print(tabrakan)


#PRsoal1
# empatdigit = int(input('input: '))
# cyclic = (empatdigit%100)*100 + empatdigit//100
# print(cyclic)

#PRsoal2
# import math

# x = 4
# y = 3 
# z = 2 
# w = ((x+y*z)/(x*y))**z
# print(w)



# #PRsoal4
# A = 'jihargifari'
# print(A.replace('a', ''))

#PRsoal5
# sentList = 'makan temen'
# currentWord = input('swap word: ')
# newWord = input('with word: ')

# sentList = [sentList.replace(currentWord, newWord)]

#PRsoal3
# angka1 = int(input('input 1: '))
# angka2 = int(input('input 2: '))
# digit1 = angka1//10
# digit2 = angka2//10
# digit3 = angka1%10
# digit4 = angka2%10
# print('output: ' + str('{}{}{}{}'.format(digit1, digit2, digit3, digit4)))



# x = 5
# y = '5'

# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

# x = 5
# y = '5'
# z = 6

# print(x==int(y) and int(y)<z)
# print(x==int(y) or int(y)<z)
# print(not(x==int(y) or int(y)<z))

# nilai = 
# if nilai > 80:
#    print('Excellent!')
# elif nilai >= 60 and nilai <= 80:
#    print('Good job!')
# else:
#    print("Don't give up!")

# angka = int(input('Masukkan angka: '))
# if angka 

# angka = int(input('masukkan angka : '))
# if angka%2 == 1 :
#     print('Angka {} tergolong bilangan GANJIL!'.format(angka))
# else :
#     print('Angka {} tergolong bilangan GENAP!'.format(angka))


# massa = float(input('Masukkan Massa(kg): '))
# tinggi = int(input('Masukkan Tinggi(cm): '))
# IMT = massa/(tinggi/100)**2
# if IMT < 18.5:
#     k= 'Berat badan KURANG!'
# elif (IMT >= 18.5 and IMT < 25): 
#     k= 'Berat badan IDEAL!'
# print('massa {} kg & tinggi {} cm'.format(massa, tinggi)  

# angka = 1
# while angka <= 10:
#    print(angka)
#    angka *= 2

# listItem = list(range(1,11,2))
# print(listItem)
# for item in range(3, 8):
# 	for
#     print(item)

# z=''
# for i in range(5):
#    z += ' * '
# print(z)

#SOAL1
# z=''
# for i in range(5,0,-1):
#    for j in range(1, i+1):
#       z += ' * '
#    z += '\n'
# print(z)

# #SOAL2
# z=''
# for i in range(5,0,-1):
#    for j in range(1, i+1):
#       z += ' * '
#    z += '\n'
# for m in range(2,6,1):
#     for l in range(2, m+2):
#         z += ' * '
#     z += '\n'
# print(z)

#SOAL3
# z= ''
# for i in (range(10)):
#     print((' * '*(1+2*i)).center(1+6*10))

# print(z)

#SOAL4
# z= ''
# for i in reversed(range(10)):
#     print((' * '*(1+2*i)).center(1+6*10))

# print(z)

#SOAL5
# z = ''
# for i in (range(5)):
#     print((' * '*(1+2*i)).center(1+6*20))
# for i in reversed(range(5)):
#     print((' * '*(1+2*i)).center(1+6*20))
# print(z)

# #loop statement
# print('Contoh Break')
# for i in range(10):
#     if i == 7 :
#         break
#     else:
#         print(i)

# a = list(range(0,3))
# print('contoh pass')
# for item in a :
#     if not item :
#         pass
#     else:
#         print(item *2)
#     print(item)

# def contoh() :
#     print('Halo Dunia!')
# contoh()

# x = 10
# y = 50
# def contoh(a, b) :
#    print(a)
#    print(b)
# contoh(a = x+4,b=y+4)

# def namaku(nama) :
#    print(nama + ' Susilo')
# namaku('Adi')
# namaku('Budi')
# namaku('Caca')
# namaku('Dedi')

# def namaku(nama) :
#     print('Muhammad ' + nama)
# namaku('jihar')
# namaku('ghifari')
# namaku('ihsan')

# def data(x,y,z) :
#    print(x+' lahir tahun '+y + ' bulan ' + z)
# data('Adi','1990', 'februari')
# data('Budi','1991', 'januari')
# data('Caca','1992', 'februari')
# data('Dedi','1993', 'maret')

# def total(x,y,z) :
#     z = x + y - z
#     return z
# print(total(2,3,4))


# def kali(x) :
# #     if (x < 2) :
# #        return 1
# #     else :
# #        return (x * tiga())
# # def tiga() :
# #     return 4
# # print(kali(15))


def latihan(x,y,z):
    if (z == 'kali') :
        return x*y
    elif (z == 'bagi') :
        return x/y
    elif (z == 'tambah') :
        return x+y
    elif (z == 'kurang') : 
        return x-y
    else :
        return 'salah input'
tambah = latihan(10,5,'tambah')
kali = latihan(10,5,'kali')
bagi = latihan(10,5,'bagi')
kurang = latihan(10,5,'kurang')

print(latihan(10,4,'bagi'))

#Belajar tipe data LIST
# mobil = ['alya','xenia',12, True, False, ['Jeruk', 12.5]]
# print(mobil)

# mobil.append('BMW')
# print(mobil)
# mobil[-1] = 'mercedes'
# print(mobil)

# mobil[2:6] = ('kopaja', 'alphard', 'angkot', 'bajaj')
# print(mobil)

# print(mobil.pop(2))

