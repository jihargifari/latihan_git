buah = ['jeruk', 'nanas', 'apel', 'mangga', 'pir', 'kiwi', 'semangka']
mobil = ['avanza', 'kijang', 'terios', 'BMW', 'mercy', 'brio', 'alya']
# for no, isi in enumerate(buah):
#     print('{}. {}'.format(no+1, isi))
for i, j, k in zip(buah, mobil, range(1,8,1)):
    print(i + ' ' + j + ' ' + str(k))