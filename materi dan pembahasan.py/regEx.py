import re
# months = ['February', 'March' , 'April', 'may', 'june']
# for month in months :
#     if re.search(r'a', month) :
#         print(month)

# hello_list = ['ab', 'aob', 'helloworllld', '1heloworld', 'super word']
# for word in hello_list :
#     if re.search(r'worl{1}d', word):
#         print(word)


# # PAKE FINDALL -> HASILNYA LIST
# string = 'february march April May June 123 456 45.3 2.36'
# match = re.findall(r'[a-zA-Z]+|\d+\.\d+|1\d+', string)
# print(match)

# # multiline case
# word = 'i'

# # re.sub untuk mensubtitusi atau me-replace
# word = "Where 1 cat owner's is never been there!!"
# print(re.sub( r'[^a-zA-Z\']',' ', word))

# #re.split 
# word = 'Only 2 time but 1 is enough. The ! is another sign'
# print(re.split(r'[0-9.!]', word))

# # regex re.compile
# regex = re.compile('[a-zA-Z0-9]+')
# word = "do not feed the monkey's. it is really bad!!!"
# print(regex.findall(word))
# print(regex.sub('', word))

string = 'cat dog kamper monkeye nlakhs jaja jaja jihar@abcde.com harz.co@gmail.com rarara@google.com'

email = re.compile()

def find_email(string) :

