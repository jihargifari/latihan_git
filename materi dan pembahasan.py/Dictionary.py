# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"]}
# print(d["key1"])
# print(d["key2"])
# print(d["kucing"])
# print(d["kucing"][1])
# # #dictionary adalah tipe data yang dapat menampung tipe data apapun, seperti List. perbedaannya adalah,
# # kali ini kita bisa menamai indeks nya. 

# #cara memberi nama indeks dari suatu valuu ialah 'nama key : value'
# for i in d :
#     print (i)
# # bila dictionary di loop maka yang ke-loop adalah key nya

# # ada banyak method di dictionary, diantaranya adalah :
# print(d.keys()) #untuk memunculkan nama2 key nya
# print(list(d.keys())) #untuk mengubah dictionary menjadi list
# print('item2' in list(d.values())) #untuk mastiin ada atau ngga suatu kata tertentu
# print(d.values()) #untuk mendapatkan value nya aja
# print(d.items())

# for val in d.items() :
#     print(val)

# bila ingin menambah isi di dictionary, ga bisa di append kayak di list. caranya adalah seperti ini
# buat key baru
# d["key3"] = "kucing meong"

# d["key1"] = d["key1"] + " kucing garong"
# print(d)

# # Dictionary juga memiliki dictionary comprehension
# list_lain = ["buah", "mangga", "jeruk"]
# dictio = {key:val for val, key in enumerate(list_lain)}
# print(dictio)

#LATIHAN 
#user memasukkan sebuah kalimat bebas, misal 'saya mau makan nasi goreng siang ini dan mau makan nasi liwet nanti malam'
#buat sebuah program yang dapat mencari berapa banyak jumlah pengulangan masing2 kata

kata = input("Masukkan Kata: ")
dict_words = {}
List_word = [word.capitalize() for word in kata.split(" ")]

for word in List_word:
    if word in (dict_words.keys()):
        dict_words[word] += 1
    else :
        dict_words[word] = 1 

for k,j in dict_words.items() :
    print('Kata {} muncul sebanyak {} kali'.format(k,j)) 

#PR : 
1. pesan tiket
2. lihat history
3. keluar

1 :
List film 
pilih film
jadwal (siang/malam)
jumlah(berapa kali)
posisi row dan seat(2 x 10)

2: 

