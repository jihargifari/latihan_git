n_num = [1,3,3,3,4,4,2,4,10]

# Instruction : Find mean, median, mode, variance, std dev, skewness, and excess kurtosis! 

# mean
n = len(n_num)
get_sum = sum(n_num)
mean = get_sum/n
# print(mean)
# median
n_num.sort()
if n % 2 == 0 :
    median1 = n_num[n//2]
    median2 = n_num[n//2-1]
    median = (median1 + median2)/2
else :
    median = n_num[n//2]
# print (median)

# mode
from collections import Counter
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v==max(list(data.values()))]

if len(mode) == n :
    get_mode = 'no mode found'
else :
    get_mode = mode
# print(get_mode)

# variance
variance = sum((xi - mean) ** 2 for xi in n_num) / len(n_num)
# print(variance)

# standar deviation
std_dev = variance**0.5
# print(std_dev)

# skewness 
skew = ((sum((xi - mean) ** 3 for xi in n_num))/n) / std_dev ** 3
# print(skew)

#excess kurtosis
kurt =  (((sum((xi - mean) ** 4 for xi in n_num))/n) / std_dev ** 4) - 3
# print(kurt)

find = input('insert measurement: ')
if find == 'mean' :
    print(mean)
elif find == 'median' :
    print(median)
elif find == 'mode' or find == 'modus' :
    print(mode)
elif find == 'variance' :
    print(variance)
elif find == 'standar deviation' :
    print(std_dev)
elif find == 'skewness' :
    print(skew)
elif find == 'excess kurtosis' :
    print(kurt)
else : 
    print('invalid input')

