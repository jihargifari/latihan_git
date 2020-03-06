
# soal 2
def spinWord(s):
    word = []
    for i in s.split():
        if len(i) >= 5:
            word.append(i(::-1))
        else :
            word.append(i)
        # print(word)
    return ' '.join(word)        
# s = "hello"
# print(reversed(s))

# # spinWord = input("insert Word: ")
# # spinedWord = spinWord.split
# # print(spinedWord)

# txt = "Hey Fellow Warrior"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split(' ')

# print(x)




# # # soal3
# # list = ([False, 1,0,1,2,0,1,3,'a'])

# # print(str(list))

# def moveZeros(list) :
#     new_list = []
#     zero = 0 
#     for i in list :
#         if i !=0 or type(i) == type(false) :
#             new_list.append(i)
#         else : 
#             zero += 1
#     for i in range(zero) :
#         new_list.append