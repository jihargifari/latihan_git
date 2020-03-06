# contoh = [i*j for i in range(5) for j in range(2)]
# print (contoh)
# # (sebenernya sama kayak:) 
# # for i in range(5):
# #     for j in range(2):
# #         i*j
# contoh = [str(i*j) if i<3 or i == 4 else i+j for i in range(5) for j in range(2)]
# print(contoh)

# buah = ['jeruk', 'nanas', 'apel', 'mangga', 'pir', 'kiwi', 'semangka']
# # CARA BIASA
# # for i in buah:
# #     if (len(i)>4):
# #         print(i[:2])
# #     else :
# #         print('buah lain')
# #CARA LIST_COMPREHENSION
# buah = [i[:2] if (len(i)>4) else 'buah lain' for i in buah]
# print(buah)

# varian_angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# angka = int(input('masukkan angka: '))
# if (angka == 0) :
#     print(' __')
#     print('|  |')
#     print('|__|')
# elif (angka == 1) :
#     print('|')
#     print('|')
# else :
#     print('nanti')
# if (angka == int(varian_angka[0])) :
#     print(' __')
#     print('|  |')
#     print('|__|')
# else :
#     print('nanti')
# print((varian_angka[5:]))

# PR4 :
# 1. buat angka kotak 4x4
# 2. bisa diputer, input ke arah mana dan berapa kali
# 3. output akan berputar sesuai input
# 4. coba lagi?(y/n) terima kasih
# hint : pakai loop dan list







