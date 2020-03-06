# t = (1, [0, 'test'], {'a1':True})
# print(type(t))
# print(t[1])
# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1] = 'mark'
# print(t[1])

# l = [True, 1,3,1,2,2,3, 'a', 'a', True, True, False,'b', 1.4, 1.4]
# print(list(set(l))[1:])
# # # print(type(s))

# def times2(num):
#     return num *2

# listNum = [times2(item) for item in range(1,6)]
# print(listNum)

# # print('Without Lambda')
# # listNum = [1,2,3,4,5]
# # listNum = list(map(str, listNum))
# # print(listNum)

# # print('With Lambda')
# # listNum = [1,2,3,4,5]
# # listNum = list(map(lambda z: str(z*2) if z < 3 else z/2, listNum))
# # print(listNum)

# def genap(num):
#     return num % 2 == 0

# # print('Without Lambda')
# # listNum = [1,2,3,4,5]
# # listNum = list(filter(genap, listNum))
# # print(listNum)    

# # print('With Lambda')
# # listNum = [1,2,3,4,5]
# # listNum = list(filter(lambda num: num %2 == 0, listNum))

# # listNum = 'ini string'
# # listNum = list(filter(lambda num: num != 'i', listNum))
# # print(listNum)


listNum = [1,2,3,4,5]

# #Duplikat Filter
def filterlist(function,list_container):
    hasil = []
    for i in list_container:
        if function(i):
            hasil.append(i)
    return hasil
# print(filterlist(lambda num: num %2 == 0, listNum))
# #Duplikat Map
def maplist(function,list_container):
    hasil =[]
    for item in list_container:
        hasil.append(function(item))
    return hasil

# # print(maplist(lambda num: num *2 , listNum))

# list_kata=['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']

# search = input('Search: ')
# print(filterlist(lambda x: search.lower() in x.lower(), list_kata))

# t = (1, [0, "test"], { "a1" : True },
# (0,{ "test" : 5 },2))

# print(t[3][1]['test'])  

# newList = [ 1, 3, "test1", "test2" , 2, 3, "test1" ]
# s = set(newList)
# print(s)
# print(list(s)[2])

# def fibo(urut) :

#     listData = [1,1]

#     for i in range(2,urut):

#         listData.append(listData[i-2] + listData[i-1])

#     return listData[urut-1]
# print(fibo(8))
import math;

def reverseList(theList) :

    for i in range(0, math.floor(len(theList)/2)) :

        tempList = theList[i]

        theList[i] = theList[len(theList) - 1 - i]

        theList[len(theList) - 1 - i] = tempList

    return theList

print(reverseList([1,2,3,4,5,6,7,8]))