# 1. isi list (bisa ditambah listnya(append))
    #berapa angka yang ingin dimasukkan
    # masukkan angka
    # loop 
# 2. Lihat List
    # Data List yang sudah diinput
    # nambah sesuai yang diappend
# 3. short list ascending
    # Data dari kecil ke gede ( <= , >=)
# 4. short list descending
    # Data dari gede ke kecil ( <= , >=)
# 5. Nilai tertinggi dan terendah
# 6. jumlah ganjil genap
    #berapa banyak angka ganjil dan genap
# 7. keluar
    # terima kasih
    # else invalid input

def menu():
    pilih = 0
    lst = []
    while pilih != 7:
        print('''
Main Menu
1.Isi List
2.Lihat List
3.Sort List Ascending
4.Sort List Descending
5.Nilai tertinggi dan terendah
6.Jumlah Ganjil dan Genap
7.Keluar
    ''')
        pilih = int(input('Pilih yang mana?: '))             
        if pilih == 1:
            try:
                isi = int(input('Berapa kali memasukkan angka: '))
            except:
                print('Invalid Input')
                continue    
            for i in range(isi):
                try:
                    add = int(input('Masukkan angka: '))
                    lst.append(add)
                except:
                    print('Invalid Input')
                    lst = []
                    break    
        elif pilih == 2:
            print(lst)
        elif pilih == 3:
            new_list=[]
            while lst:
                themin = lst[0] 
                for i in lst: 
                    if themin > i:
                        themin = i
                new_list.append(themin)
                lst.remove(themin)
            lst = new_list
            print(lst)
        elif pilih == 4:
            new_list=[]
            while lst:
                themax = lst[0] 
                for i in lst: 
                    if themax < i:
                        themax = i
                new_list.append(themax)
                lst.remove(themax)
            lst = new_list
            print(lst)                                
        elif pilih == 5:
            themax = lst[0]
            for i in lst:
                if themax < i:
                    themax = i
            themin = lst[0]
            for i in lst:
                if themin > i:
                    themin = i
            print('Nilai tertinggi adalah {} dan nilai terendah adalah {}'.format(themax,themin))
        elif pilih == 6:
            odd = 0
            even = 0
            for i in lst:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            print('Jumlah angka Ganjil ada {} dan angka Genap ada {}'.format(odd,even))
        elif pilih == 7:
            print('Terima Kasih')
        else:
            print('Invalid Input')

#PEMBAHASAN


