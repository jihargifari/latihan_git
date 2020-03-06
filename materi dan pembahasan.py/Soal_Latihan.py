#LATIHAN FIZZBUZZ
#KALO BISA DIBAGI 3 = FIZZ
# KALO BISA DIBAGI 5 = BUZZ
# KALO BISA DIBAGI 3 DAN 5 = FIZZBUZZ
# KALO BILANGAN PRIMA(HANYA BISA DIBAGI 1 DAN ANGKA ITU SENDIRI) = FIZZPRIME
def primeNumber(num):
    for x in range(2, num-1):
        if num % x == 0 :
            return False
    else :
        return True

def fizzbuzz(n) :
    for i in range(1, n+1) :
        if (i == 1) :
            print(i)
        elif primeNumber(i) :
            print('FizzPrime')
        elif (i % 15 == 0) :
            print('FizzBuzz')
        elif (i % 5 == 0) :
            print('Buzz')
        elif (i % 3 == 0) :
            print('Fizz')
        else :
            print(i)
fizzbuzz(50)
     
#LATIHAN DATA MEASUREMENT OF CENTER & MEASUREMENT

list_angka = [1,3,3,3,4,4,2,4,10]
# print(statistic_sample(list_angka, ''))

# mean
def Mean(list_angka) :
    sum = 0
    for item in list :
        sum += item
    mean = sum / len(list)
    return mean
print(Mean(list))

median
mode
variance_pop
stdev_pop
skewness
excess_kurtosis