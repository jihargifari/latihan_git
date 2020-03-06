#SOAL1
z=''
for i in range(5,0,-1):
   for j in range(1, i+1):
      z += ' * '
   z += '\n'
print(z)

# #SOAL2
z=''
for i in range(5,0,-1):
   for j in range(1, i+1):
      z += ' * '
   z += '\n'
for m in range(2,6,1):
    for l in range(2, m+2):
        z += ' * '
    z += '\n'
print(z)

#SOAL3
z= ''
for i in (range(10)):
    print((' * '*(1+2*i)).center(1+6*10))

print(z)

#SOAL4
z= ''
for i in reversed(range(10)):
    print((' * '*(1+2*i)).center(1+6*10))

print(z)

#SOAL5
z = ''
for i in (range(5)):
    print((' * '*(1+2*i)).center(1+6*20))
for i in reversed(range(5)):
    print((' * '*(1+2*i)).center(1+6*20))
print(z)
