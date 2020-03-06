
# PR8 CLASS RAMAL
# MENU RAMALAN : 1) PEKERJAAN, 2) KESEHATAN, 3) PERCINTAAN, 4) KELUAR
# MASUKKAN PILIHAN
import random 
class ramalan :
    def __init__(self, occupancy, health, love): 
        self.pekerjaan = occupancy
        self.kesehatan = health
        self.percintaan = love

    def getMenu(self) :
        print('App Ramalan Terkini')
        print('1. Ramalan {}'.format(self.pekerjaan))
        print('2. Ramalan {}'.format(self.kesehatan))
        print('3. Ramalan {}'.format(self.percintaan))
        print('4. keluar')

    def hasilRamalan(self) :
        pilihan = int(input('Masukkan pilihan: '))
        # uang = masuk(10000)
        if pilihan == 1:
            print('Hasil ramalan : anda akan {}'.format(random.choice(ramalan_pekerjaan)))
        elif pilihan == 2 :
            print('Hasil ramalan : anda akan {}'.format(random.choice(ramalan_kesehatan)))
        elif pilihan == 3 :
            print('Hasil ramalan : anda akan {}'.format(random.choice(ramalan_percintaan)))
        elif pilihan == 4 :
            print('Terima Kasih')
        else :
            print('invalid input')


ramal=ramalan('Pekerjaan', 'Kesehatan', 'Percintaan')
ramalan_pekerjaan = ['Dipecat', 'Ga naik gaji', 'Gitu-gitu aja', 'Naik gaji', 'Jadi Bos']
ramalan_kesehatan = ['Mati','kanker','flu', 'sehat terus', 'jadi sixpack!']
ramalan_percintaan = ['Jomblo selamanya','menikah tua','menikah di umur 30-an', 'cepat nikah', 'menikah dan bahagia selamanya']

ramal.getMenu()
ramal.hasilRamalan()
