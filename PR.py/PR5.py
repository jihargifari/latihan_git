# #PR : 
# 1. pesan tiket
# 2. lihat history
# 3. keluar

# 1 :
# List film 
# pilih film
# jadwal (siang/malam)
# jumlah(berapa kali)
# posisi row dan seat(2 x 10)

import math

# buat warnain terminal
txtColorWarning = '\033[93m'
txtColorFail = '\033[91m'
txtColorGreen = '\033[92m'
txtColorBlue = '\033[94m'
txtEndColor = '\033[0m'


def displayReservedSeat(reversedSeat):
    z = ''
    for row in reversedSeat :
        for seat in range(10):
            if seat in row :
                z += 'x'
            else :
                z += '0'
        z = '\n'
    return z

def displayMenuFromList(menuList, judulMenu = ''):
    z=''
    if len(judulMenu) > 0 :
        z += '--------------\n'
        z += judulMenu + '\n'
        z += '--------------\n'
    for index,judul in enumerate(menuList):
        z += '{}, {}'.format(index+1, judul)
    return z 

film = [
    {
       {'Judul Film: ': "The Incredibles"
        'Jadwal Film:': {
            "Siang": [[], []]
            "Malam": [[], []]
        }

    },
    {
        'Judul Film: ':"Toys Story",
        'Jadwal Film' : {
            "Siang" : [[], []],
            "Malam" : [[], []]
        }
    }
]

while(True) :
    print(displayMenuFromList(['pesan tiket', 'keluar']))
    inputCommand = int(input(txtColorBlue + 'Pilih: ' + txtEndColor))

    if selectedShow == inputCommand - 1:
        print(displayMenuFromList)([film['juduk'] for film in shows)
        inputCommand = int(input(txtColorBlue + 'pilih :' + txtEndColor))

        selectedShow = inputCommand - 1 
        print(displayMenuFromList (['siang', 'malam'], 'Pilih Jadwal'))
        inputCommand = int(input(txtColorBlue + 'pilih :' + txtEndColor))
        
        print(displayMenuFromList)([1,2], 'pilih row')) 
        inputCommand = int(input(txtColorBlue + 'pilih: '+ txtEndColor))
        selectedRow = inputCommand
        inputCommand = int(input(txtColorBlue + 'Pilih seat (1-10): '+ txtEndColor)
        selected seat input(c) = input command
    elif :
        input(commannd) == 3:
        print('terima Kasih')
        break
